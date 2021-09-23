## Overview

This model detects humans and their poses in a given image. The model first detects the humans in the input image and then identifies the body parts, including nose, neck, eyes, shoulders, elbows, wrists, hips, knees, and ankles. Next, each pair of associated body parts is connected by a pose line. The pose lines are assembled into full body poses for each of the humans detected in the image. The model is based on the TF implementation of [OpenPose model](https://github.com/mananrai/Tensorflow-Openpose).

## Model Metadata

| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- |
| Vision | Human Pose Estimation | Multi | Tensorflow | [COCO](http://cocodataset.org) | Image File |

## References

* _Zhe Cao, Tomas Simon, Shih-En Wei, Yaser Sheikh,_ ["Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields"](https://arxiv.org/abs/1611.08050), CVPR 2017.

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| Model GitHub Repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Human-Pose-Estimator/blob/master/LICENSE) |
| Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/mananrai/Tensorflow-Openpose/blob/master/LICENSE) |
| Test assets | Various | [Samples README](https://github.com/IBM/MAX-Human-Pose-Estimator/blob/master/samples/README.md) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:

  ```
  docker run -it -p 5000:5000 codait/max-human-pose-estimator
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-human-pose-estimator` as the image name.

* Deploy on Kubernetes:

  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Human-Pose-Estimator/master/max-human-pose-estimator.yaml
  ```
  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Human-Pose-Estimator#run-locally)

## Example Usage

You can test or use this model

 - [using cURL](#test-the-model-using-curl)
 - [in a Node-RED flow](#test-the-model-in-a-node-red-flow)
 - [in CodePen](#test-the-model-in-codepen)
 - [in a serverless app](#test-the-model-in-a-serverless-app)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example if running locally:

```
curl -F "image=@samples/p3.jpg" -XPOST http://localhost:5000/model/predict
```

You should see a JSON response like that below:

```
{
  "status": "ok",
  "predictions": [
    {
      "human_id": 0,
      "pose_lines": [
        {
          "line": [
            110,
            53,
            91,
            53
          ]
        },
        {
          "line": [
            110,
            53,
            129,
            50
          ]
        },
        .
        .
        .
        {
          "line": [
            114,
            35,
            119,
            32
          ]
        }
      ]
    }
  ]
}
```

The information returned from the model can be used to construct and visualize pose lines for the humans detected in the
image, such as shown in the example below. For more details see the [GitHub README](https://github.com/IBM/MAX-Human-Pose-Estimator/blob/master/README.md).

![Pose Line Example](https://raw.githubusercontent.com/IBM/MAX-Human-Pose-Estimator/master/docs/pose-lines.png)

### Test the model in a Node-RED flow

Complete the [node-red-contrib-model-asset-exchange](https://github.com/CODAIT/node-red-contrib-model-asset-exchange)
module setup instructions and import the `human-pose-estimator` getting started flow.

### Test the model in CodePen

Learn how to send an image to the model and how to render the results in [CodePen](https://codepen.io/collection/DzdpJM/#).

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.

## Links

* [Use your arms to make music](https://developer.ibm.com/patterns/making-music-with-the-max-human-pose-estimator-and-tensorflowjs/) This interactive example application was built using a TensorFlow.js version of this model.
* [Build a web app that recognizes yoga poses using a model from the Model Asset Exchange](https://developer.ibm.com/patterns/build-a-web-application-that-recognizes-yoga-poses-using-a-model-from-the-model-asset-exchange/)

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
