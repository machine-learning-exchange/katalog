# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Robustness check module."""

import numpy as np
import numpy.linalg as la
from minio import Minio

import torch
import torch.utils.data
from torch.autograd import Variable

from art.classifiers.pytorch import PyTorchClassifier
from art.attacks.fast_gradient import FastGradientMethod

import zipfile
import importlib
import re


def get_metrics(model, x_original, x_adv_samples, y):
    model_accuracy_on_non_adversarial_samples, y_pred = evaluate(model, x_original, y)
    model_accuracy_on_adversarial_samples, y_pred_adv = evaluate(model, x_adv_samples, y)

    pert_metric = get_perturbation_metric(x_original, x_adv_samples, y_pred, y_pred_adv, ord=2)
    conf_metric = get_confidence_metric(y_pred, y_pred_adv)

    data = {
        "model accuracy on test data": float(model_accuracy_on_non_adversarial_samples),
        "model accuracy on adversarial samples": float(model_accuracy_on_adversarial_samples),
        "confidence reduced on correctly classified adv_samples": float(conf_metric),
        "average perturbation on misclassified adv_samples": float(pert_metric)
    }
    return data, y_pred, y_pred_adv


# Compute the accuaracy and predicted label using the given test dataset
def evaluate(model, X_test, y_test):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    test = torch.utils.data.TensorDataset(Variable(torch.FloatTensor(X_test.astype('float32'))), Variable(torch.LongTensor(y_test.astype('float32'))))
    test_loader = torch.utils.data.DataLoader(test, batch_size=64, shuffle=False)
    model.eval()
    correct = 0
    accuracy = 0
    y_pred = []
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            predictions = torch.softmax(outputs.data, dim=1).detach().numpy()
            correct += predicted.eq(labels.data.view_as(predicted)).sum().item()
            y_pred += predictions.tolist()
        accuracy = 1. * correct / len(test_loader.dataset)
    y_pred = np.array(y_pred)
    return accuracy, y_pred


def get_perturbation_metric(x_original, x_adv, y_pred, y_pred_adv, ord=2):
    idxs = (np.argmax(y_pred_adv, axis=1) != np.argmax(y_pred, axis=1))

    if np.sum(idxs) == 0.0:
        return 0

    perts_norm = la.norm((x_adv - x_original).reshape(x_original.shape[0], -1), ord, axis=1)
    perts_norm = perts_norm[idxs]

    return np.mean(perts_norm / la.norm(x_original[idxs].reshape(np.sum(idxs), -1), ord, axis=1))


# This computes the change in confidence for all images in the test set
def get_confidence_metric(y_pred, y_pred_adv):
    y_classidx = np.argmax(y_pred, axis=1)
    y_classconf = y_pred[np.arange(y_pred.shape[0]), y_classidx]

    y_adv_classidx = np.argmax(y_pred_adv, axis=1)
    y_adv_classconf = y_pred_adv[np.arange(y_pred_adv.shape[0]), y_adv_classidx]

    idxs = (y_classidx == y_adv_classidx)

    if np.sum(idxs) == 0.0:
        return 0

    idxnonzero = y_classconf != 0
    idxs = idxs & idxnonzero

    return np.mean((y_classconf[idxs] - y_adv_classconf[idxs]) / y_classconf[idxs])


def robustness_check(object_storage_url, object_storage_username, object_storage_password,
                     data_bucket_name, result_bucket_name, model_id,
                     feature_testset_path='processed_data/X_test.npy',
                     label_testset_path='processed_data/y_test.npy',
                     clip_values=(0, 1),
                     nb_classes=2,
                     input_shape=(1, 3, 64, 64),
                     model_class_file='model.py',
                     model_class_name='model',
                     LossFn='',
                     Optimizer='',
                     epsilon=0.2):

    url = re.compile(r"https?://")
    cos = Minio(url.sub('', object_storage_url),
                access_key=object_storage_username,
                secret_key=object_storage_password,
                secure=False)

    dataset_filenamex = "X_test.npy"
    dataset_filenamey = "y_test.npy"
    weights_filename = "model.pt"
    model_files = model_id + '/_submitted_code/model.zip'

    cos.fget_object(data_bucket_name, feature_testset_path, dataset_filenamex)
    cos.fget_object(data_bucket_name, label_testset_path, dataset_filenamey)
    cos.fget_object(result_bucket_name, model_id + '/' + weights_filename, weights_filename)
    cos.fget_object(result_bucket_name, model_files, 'model.zip')

    # Load PyTorch model definition from the source code.
    zip_ref = zipfile.ZipFile('model.zip', 'r')
    zip_ref.extractall('model_files')
    zip_ref.close()

    modulename = 'model_files.' + model_class_file.split('.')[0].replace('-', '_')

    '''
    We required users to define where the model class is located or follow
    some naming convention we have provided.
    '''
    model_class = getattr(importlib.import_module(modulename), model_class_name)

    # load & compile model
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model = model_class().to(device)
    model.load_state_dict(torch.load(weights_filename, map_location=device))

    # Define Loss and optimizer function for the PyTorch model
    if LossFn:
        loss_fn = eval(LossFn)
    else:
        loss_fn = torch.nn.CrossEntropyLoss()
    if Optimizer:
        optimizer = eval(Optimizer)
    else:
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # create pytorch classifier
    classifier = PyTorchClassifier(clip_values, model, loss_fn, optimizer, input_shape, nb_classes)

    # load test dataset
    x = np.load(dataset_filenamex)
    y = np.load(dataset_filenamey)

    # craft adversarial samples using FGSM
    crafter = FastGradientMethod(classifier, eps=epsilon)
    x_samples = crafter.generate(x)

    # obtain all metrics (robustness score, perturbation metric, reduction in confidence)
    metrics, y_pred_orig, y_pred_adv = get_metrics(model, x, x_samples, y)

    print("metrics:", metrics)
    return metrics
