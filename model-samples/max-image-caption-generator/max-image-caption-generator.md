## Overview

This model generates captions from a fixed vocabulary that describe the contents of images in the [COCO Dataset](http://cocodataset.org/#home). The model consists of an _encoder_ model - a deep convolutional net using the Inception-v3 architecture trained on [ImageNet-2012 data](http://www.image-net.org/challenges/LSVRC/2012/) - and a _decoder_ model - an LSTM network that is trained conditioned on the encoding from the image _encoder_ model. The input to the model is an image, and the output is a sentence describing the image content.

The model is based on the [Show and Tell Image Caption Generator Model](https://github.com/tensorflow/models/tree/archive/research/im2txt).

## Model Metadata

| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- |
| Vision | Image Caption Generator | General | TensorFlow | [COCO](http://cocodataset.org/#home) | Images |

## References

* _O. Vinyals, A. Toshev, S. Bengio, D. Erhan_, ["Show and Tell: Lessons learned from the 2015 MSCOCO Image Captioning Challenge"](https://arxiv.org/abs/1609.06647), IEEE transactions on Pattern Analysis and Machine Intelligence, 2016.
* [im2txt TensorFlow Model GitHub Page](https://github.com/tensorflow/models/tree/archive/research/im2txt)
* [COCO Dataset Project Page](http://cocodataset.org/#home)

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| This repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Image-Caption-Generator/blob/master/LICENSE) |
| Model Weights | [MIT](https://opensource.org/licenses/MIT) | [Pretrained Show and Tell Model](https://github.com/KranthiGV/Pretrained-Show-and-Tell-model) |
| Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [im2txt](https://github.com/tensorflow/models/tree/archive/research/im2txt) |
| Test assets | Various | [Asset README](https://github.com/IBM/MAX-Image-Caption-Generator/blob/master/assets/README.md) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:

  ```
  docker run -it -p 5000:5000 codait/max-image-caption-generator
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-image-caption-generator` as the image name.

* Deploy on Kubernetes:

  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Image-Caption-Generator/master/max-image-caption-generator.yaml
  ```
  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Image-Caption-Generator#run-locally)

## Example Usage

You can test or use this model

 - [using cURL](#test-the-model-using-curl)
 - [in a Node-RED flow](#test-the-model-in-a-node-red-flow)
 - [in CodePen](#test-the-model-in-codepen)
 - [in a serverless app](#test-the-model-in-a-serverless-app)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example if running locally:

```
curl -F "image=@assets/surfing.jpg" -X POST http://127.0.0.1:5000/model/predict
```

```json
{
  "status": "ok",
  "predictions": [
    {
      "index": "0",
      "caption": "a man riding a wave on top of a surfboard .",
      "probability": 0.038827644239537
    },
    {
      "index": "1",
      "caption": "a person riding a surf board on a wave",
      "probability": 0.017933410519265
    },
    {
      "index": "2",
      "caption": "a man riding a wave on a surfboard in the ocean .",
      "probability": 0.0056628732021868
    }
  ]
}
```

### Test the model in a Node-RED flow

Complete the [node-red-contrib-model-asset-exchange](https://github.com/CODAIT/node-red-contrib-model-asset-exchange) module setup instructions and import the `image-caption-generator` getting started flow.

### Test the model in CodePen

Learn how to send an image to the model and how to render the results in [CodePen](https://codepen.io/collection/DzdpJM/#).

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.

## Links

* [Image Caption Generator Web App](https://developer.ibm.com/patterns/create-a-web-app-to-interact-with-machine-learning-generated-image-captions/): A reference application created by the IBM CODAIT team that uses the Image Caption Generator

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
