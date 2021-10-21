## Overview

Given a body of text (context) about a subject and questions about that subject, the model will answer questions based on the given context.

The model is based on the [BERT model](https://github.com/google-research/bert).

## Model Metadata

| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- |
| Natural Language Processing (NLP) | Question and Answer | General | TensorFlow | [SQuAD 1.1](https://rajpurkar.github.io/SQuAD-explorer/) | Text |

## References

* _J. Devlin, M. Chang, K. Lee, K. Toutanova_, ["BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"](https://arxiv.org/abs/1810.04805), arXiv, 2018.
* [Google BERT](https://github.com/google-research/bert)
* [SQuAD Dataset](https://rajpurkar.github.io/SQuAD-explorer/) and version 1.1 on the [Google BERT](https://github.com/google-research/bert) repo

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| Model GitHub repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Question-Answering/blob/master/LICENSE) |
| Fine-tuned Model Weights |  [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Question-Answering/blob/master/LICENSE)
| Pre-trained Model Weights |  [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/google-research/bert/blob/master/LICENSE)
| Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/google-research/bert/blob/master/LICENSE) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:

```
docker run -it -p 5000:5000 codait/max-question-answering
```

* Deploy on Kubernetes:

```
kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Question-Answering/master/max-question-answering.yaml
```

A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Question-Answering#run-locally)

## Example Usage

You can test or use this model

* [using cURL](#test-the-model-using-curl)
* [in a notebook](#test-the-model-in-a-notebook)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example if running locally:

```shell
curl -X POST "http://localhost:5000/model/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"paragraphs\": [{ \"context\": \"John lives in Brussels and works for the EU\", \"questions\": [\"Where does John Live?\",\"What does John do?\",\"What is his name?\" ]},{ \"context\": \"Jane lives in Paris and works for the UN\", \"questions\": [\"Where does Jane Live?\",\"What does Jane do?\" ]}]}"
```

```json
{
  "status": "ok",
  "predictions": [
    [
      "Brussels",
      "works for the EU",
      "John"
    ],
    [
      "Paris",
      "works for the UN"
    ]
  ]
}
```

### Test the model in a notebook

The [demo notebook](https://github.com/IBM/MAX-Question-Answering/blob/master/samples/demo.ipynb) walks through how to use the
model to answer questions on a given corpus of text. By default, the notebook uses the
[hosted demo instance](http://max-question-answering.codait-prod-41208c73af8fca213512856c7a09db52-0000.us-east.containers.appdomain.cloud),
but you can use a locally running instance.

Run the following command from the model repo base folder, in a new terminal window:

```
jupyter notebook
```

This will start the notebook server. You can launch the demo notebook by clicking on `samples/demo.ipynb`.

## Options available for training this model

This model can be trained using the following mechanisms:

* Train on IBM Cloud - Watson Machine Learning: follow the instructions in the [model training README on GitHub](https://github.com/IBM/MAX-Question-Answering/tree/master/training).

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
