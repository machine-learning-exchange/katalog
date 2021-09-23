## Overview

This model is able to detect whether a text fragment leans towards a positive or a negative sentiment. The underlying neural network is based on the [pre-trained BERT-Base, English Uncased](https://github.com/google-research/bert/blob/master/README.md) model and was finetuned on the [IBM Claim Stance Dataset](http://www.research.ibm.com/haifa/dept/vst/debating_data.shtml).

Optimal input examples for this model are short strings (preferably a single sentence) with correct grammar, although not a requirement.

## Model Metadata
| Domain | Application | Industry  | Framework | Training Data | Input Data |
| --------- | --------  | -------- | --------- | --------- | --------------- |
| Natural Language Processing (NLP) | Sentiment Analysis | General | TensorFlow | [IBM Claim Stance Dataset](http://www.research.ibm.com/haifa/dept/vst/debating_data.shtml) | Text |

## Benchmark
In the table below, the prediction accuracy of the model on the test sets of three different datasets is listed.

The first row showcases the generalization power of our model after finetuning on the IBM Claims Dataset.
 The Sentiment140 (Tweets) and IMDB Reviews datasets are only used for evaluating the transfer-learning capabilities of this model. The implementation in this repository was **not** trained or finetuned on the Sentiment140 or IMDB reviews datasets.

The second row describes the performance of the BERT-Base (English - Uncased) model when finetuned on the specific task. This was done simply for reference, and the weights are therefore not made available.


The generalization results (first row) are very good when the input data is similar to the data used for finetuning (e.g. Sentiment140 (tweets) when finetuned on the IBM Claims Dataset). However, when a different style of text is given as input, and with a longer median length (e.g. multi-sentence IMDB reviews), the results are not as good.

| Model Type | IBM Claims | Sentiment140 | IMDB Reviews |
| ------------- | --------  | -------- | -------------- |
| This Model <br> (finetuned on IBM Claims) | 94% | 83.84% | 81% |
| Models finetuned on the specific dataset | 94% | 84% | 90% |

## References
* _J. Devlin, M. Chang, K. Lee, K. Toutanova_, [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805), arXiv, 2018.
* [Google BERT repository](https://github.com/google-research/bert)
* [IBM Claims Stance Dataset](http://www.research.ibm.com/haifa/dept/vst/debating_data.shtml#Project) and [IBM Project Debater](https://www.research.ibm.com/artificial-intelligence/project-debater/)

## Licenses
| Component | License | Link  |
| ------------- | --------  | -------- |
| Model GitHub repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Text-Sentiment-Classifier/blob/master/LICENSE) |
| Finetuned Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Text-Sentiment-Classifier/blob/master/LICENSE) |
| Pre-trained Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/google-research/bert/blob/master/LICENSE) |
| Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/google-research/bert/blob/master/LICENSE) |
| IBM Claims Stance Dataset for finetuning | [CC-BY-SA](http://creativecommons.org/licenses/by-sa/3.0/) | [LICENSE 1](http://www.research.ibm.com/haifa/dept/vst/debating_data.shtml#Project) <br> [LICENSE 2](https://en.wikipedia.org/wiki/Wikipedia:Copyrights#Reusers.27_rights_and_obligations)|

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:

  ```
  docker run -it -p 5000:5000 codait/max-text-sentiment-classifier
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-text-sentiment-classifier` as the image name.

* Deploy on Kubernetes:

  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Text-Sentiment-Classifier/master/max-text-sentiment-classifier.yaml
  ```

  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Text-Sentiment-Classifier#run-locally)

## Example Usage

You can test or use this model
 - [using cURL](#test-the-model-using-curl)
 - [in a serverless app](#test-the-model-in-a-serverless-app)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example:

```
curl -d "{ \"text\": [ \"The Model Asset Exchange is a crucial element of a developer's toolkit.\" ]}" -X POST "http://localhost:5000/model/predict" -H "Content-Type: application/json"
```

You should see a JSON response like that below:

```json
{
  "status": "ok",
  "predictions": [
    [
      {
        "positive": 0.9977352619171143,
        "negative": 0.0022646968718618155
      }
    ]
  ]
}
```

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.


## Options available for training this model

This model can be trained using the following mechanisms:

* Train on IBM Cloud - Watson Machine Learning: follow the instructions in the [model training README on GitHub](https://github.com/IBM/MAX-Text-Sentiment-Classifier/tree/master/training).

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).