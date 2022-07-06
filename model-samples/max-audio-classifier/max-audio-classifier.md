## Overview

This model recognizes a signed 16-bit PCM wav file as an input, generates embeddings, applies
[PCA transformation/quantization](https://github.com/tensorflow/models/tree/master/research/audioset#output-embeddings),
uses the embeddings as an input to a multi-attention classifier and outputs top 5 class predictions and probabilities as
output.  The model currently supports 527 classes which are part of the
[Audioset Ontology](https://research.google.com/audioset/ontology/index.html). The classes and the label_ids can be
found in [class_labels_indices.csv](https://github.com/IBM/MAX-Audio-Classifier/blob/master/samples/class_labels_indices.csv).
The model was trained on [AudioSet](https://research.google.com/audioset/) as described in the paper
['Multi-level Attention Model for Weakly Supervised Audio Classification'](https://arxiv.org/abs/1803.02353) by Yu et al.

The model has been tested across multiple audio classes, however it tends to perform best for Music / Speech categories.
This is largely due to the bias towards these classes in the training dataset (90% of audio belong to either of these
categories). Though the model is trained on data from Audioset which was extracted from YouTube videos, the model can be
applied to a wide range of audio files outside the domain of music/speech. The test assets provided along with this
model provide a broad range.

## Model Metadata
| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- |
| Audio | Classification | Multi | Keras/TensorFlow | Google AudioSet | signed 16-bit PCM WAV or MP3 audio file |

## References

* _Jort F. Gemmeke, Daniel P. W. Ellis, Dylan Freedman, Aren Jansen, Wade Lawrence, R. Channing Moore, Manoj Plakal, Marvin Ritter_,["Audio set: An ontology and human-labeled dataset for audio events"](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45857.pdf), IEEE ICASSP, 2017.

* _Qiuqiang Kong, Yong Xu, Wenwu Wang, Mark D. Plumbley_, ["Audio Set classification with attention model: A probabilistic perspective"](https://arxiv.org/pdf/1711.00927.pdf), arXiv preprint arXiv:1711.00927 (2017).

* _Changsong Yu, Karim Said Barsim, Qiuqiang Kong, Bin Yang_ , ["Multi-level Attention Model for Weakly Supervised Audio Classification"](https://arxiv.org/pdf/1803.02353.pdf), arXiv preprint arXiv:1803.02353 (2018).

* _S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold et  al._, ["CNN architectures for large-scale audio classification"](https://arxiv.org/pdf/1609.09430.pdf), arXiv preprint arXiv:1609.09430, 2016.


## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| Model Github Repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Audio-Classifier/blob/master/LICENSE) |
| Model Files | [Apache 2.0](https://github.com/tensorflow/models/blob/master/LICENSE) | [AudioSet](https://github.com/tensorflow/models/tree/master/research/audioset) |
| Model Code | [MIT](https://github.com/qiuqiangkong/audioset_classification/blob/master/LICENSE.txt) | [AudioSet Classification](https://github.com/qiuqiangkong/audioset_classification) |
| Test assets | Various | [Samples README](https://github.com/IBM/MAX-Audio-Classifier/blob/master/samples/README.md) |

## Options available for deploying this model

* Deploy from Dockerhub:

  ```
  docker run -it -p 5000:5000 codait/max-audio-classifier
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-audio-classifier` as the image name.

* Deploy on Kubernetes:

  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Audio-Classifier/master/max-audio-classifier.yaml
  ```
  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Audio-Classifier#run-locally)

## Example Usage

You can test or use this model

 - [using cURL](#test-the-model-using-curl)
 - [in a Node-RED flow](#test-the-model-in-a-node-red-flow)
 - [in CodePen](#test-the-model-in-codepen)
 - [in a serverless app](#test-the-model-in-a-serverless-app)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example if running locally:

```
curl -F "audio=@samples/thunder.wav" -XPOST http://localhost:5000/model/predict
```

```
{
    "status": "ok",
    "predictions": [
        {
            "label_id": "/m/06mb1",
            "label": "Rain",
            "probability": 0.7376469373703003
        },
        {
            "label_id": "/m/0ngt1",
            "label": "Thunder",
            "probability": 0.60517817735672
        },
        {
            "label_id": "/t/dd00038",
            "label": "Rain on surface",
            "probability": 0.5905200839042664
        }
    ]
}
```

### Test the model in a Node-RED flow

Complete the [node-red-contrib-model-asset-exchange](https://github.com/CODAIT/node-red-contrib-model-asset-exchange) module setup instructions and import the `audio-classifier` getting started flow.

### Test the model in CodePen

Learn how to send an audio clip to the model in [CodePen](https://codepen.io/codait/pen/VojGqp).

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
