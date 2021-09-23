## Overview

The model is based on the [Neural Collaborative Filtering model]([https://github.com/microsoft/recommenders]). This model can be trained on a dataset containing users, items, ratings, and timestamps and make personalized item recommendations for a given user. Once trained, the input to the model is a user ID and the output is a list of recommended item IDs sorted by estimated propensity score, in descending order. For demo purposes this model has been trained on a subset of the [MovieTweetings Dataset](https://github.com/sidooms/MovieTweetings), containing 457 users with their IDs mapped from 0 to 457 for convenience.

## Model Metadata
| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- |
| Information Retrieval | Recommendations | Commerce | TensorFlow | [MovieTweetings](https://github.com/sidooms/MovieTweetings) | CSV |

## References

* _X. He, L. Liao, H. Zhang, L. Nie, X. Hu, T. Chua_, ["Neural Collaborative Filtering"](https://arxiv.org/abs/1708.05031), WWW 2017.
* [Microsoft Recommender Systems GitHub Repo](https://github.com/microsoft/recommenders)

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| Model GitHub Repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Recommender/blob/master/LICENSE) |
| Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Recommender/blob/master/LICENSE) |
| Model Code (3rd party) | [MIT](https://opensource.org/licenses/mit-license.html) | [Microsoft Recommender Systems GitHub Repo](https://github.com/microsoft/recommenders/blob/master/LICENSE) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:

  ```
  docker run -it -p 5000:5000 codait/max-recommender
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-recommender` as the image name.

* Deploy on Kubernetes:
  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Recommender/master/max-recommender.yaml
  ```
* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Recommender#run-locally)

## Options available for training this model

This model can be trained using the following mechanisms:

* Train on IBM Cloud - Watson Machine Learning: follow the instructions in the [model training README on GitHub](https://github.com/IBM/MAX-Recommender/blob/master/training/README.md)

## Example Usage

You can test or use this model

 - [using cURL](#test-the-model-using-curl)
 - [in a serverless app](#test-the-model-in-a-serverless-app)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example if running locally:

```
$ curl -X POST "http://localhost:5000/model/predict?user_id=1&num_results=5" -H "accept: application/json"
```

```json
{
  "status": "ok",
  "predictions": [
      {
      "user": "1",
      "item": "1454468",
      "prediction": 0.995230495929718
    },
    {
      "user": "1",
      "item": "1300854",
      "prediction": 0.9938176274299622
    },
    {
      "user": "1",
      "item": "77413",
      "prediction": 0.9930911064147949
    },
    {
      "user": "1",
      "item": "1731141",
      "prediction": 0.9929673671722412
    },
    {
      "user": "1",
      "item": "363226",
      "prediction": 0.9914621710777283
    }
  ]
}
```

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.
