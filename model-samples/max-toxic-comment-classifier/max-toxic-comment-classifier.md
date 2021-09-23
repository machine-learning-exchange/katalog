## Overview

This model is able to detect 6 types of toxicity in a text fragment. The six detectable types are toxic, severe toxic, obscene, threat, insult, and identity hate. The underlying neural network is based on the [pre-trained BERT-Base, English Uncased model](https://github.com/google-research/bert/blob/master/README.md) and was finetuned on the [Toxic Comment Classification Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) using the [Huggingface BERT Pytorch repository](https://github.com/huggingface/pytorch-pretrained-BERT).

A brief definition of the six different toxicity types can be found below.

```
Toxic: very bad, unpleasant, or harmful

Severe toxic: extremely bad and offensive

Obscene: (of the portrayal or description of sexual matters) offensive or disgusting by accepted standards of morality and decency

Threat: a statement of an intention to inflict pain, injury, damage, or other hostile action on someone in retribution for something done or not done

Insult: speak to or treat with disrespect or scornful abuse

Identity hate: hatred, hostility, or violence towards members of a race, ethnicity, nation, religion, gender, gender identity, sexual orientation or any other designated sector of society
```

## Model Metadata
| Domain | Application | Industry  | Framework | Training Data | Input Data |
| --------- | --------  | -------- | --------- | --------- | --------------- |
| Natural Language Processing (NLP) | Text Classification | General | PyTorch | [Toxic Comment Classification Dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) | Text |


## Benchmark

This model achieves a column-wise ROC AUC score of 0.98355 (private score) in the [Kaggle Toxic Comment Classification Competition](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge). This implementation is trained with a maximum sequence length of 256 instead of 512 to have higher inference speed. For most applications outside of this Kaggle competition, a sequence length of 256 is more than sufficient.

## References
* _J. Devlin, M. Chang, K. Lee, K. Toutanova_, [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805), arXiv, 2018.
* [Google BERT repository](https://github.com/google-research/bert)
* [Huggingface BERT Pytorch repository](https://github.com/huggingface/pytorch-pretrained-BERT)
* [Multi-Label Text Classification using BERT - The Mighty Transformer](https://medium.com/huggingface/multi-label-text-classification-using-bert-the-mighty-transformer-69714fa3fb3d)
* [Kaggle Toxic Comment Classification](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge)

## Licenses
| Component | License | Link  |
| ------------- | --------  | -------- |
| Model GitHub repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Toxic-Comment-Classifier/blob/master/LICENSE) |
| Finetuned Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Toxic-Comment-Classifier/blob/master/LICENSE) |
| Pre-trained Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/google-research/bert/blob/master/LICENSE) |
| TensorFlow Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/google-research/bert/blob/master/LICENSE) |
| PyTorch Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/huggingface/pytorch-pretrained-BERT/blob/master/LICENSE) |
| Toxic Comment Classification Dataset | [CC0](https://creativecommons.org/share-your-work/public-domain/cc0/) | [LICENSE](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:
  ```
  docker run -it -p 5000:5000 codait/max-toxic-comment-classifier
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-toxic-comment-classifier` as the image name.

* Deploy on Kubernetes:
  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Toxic-Comment-Classifier/master/max-toxic-comment-classifier.yaml
  ```
  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Toxic-Comment-Classifier#run-locally)

## Example Usage

You can test or use this model
 - [using cURL](#test-the-model-using-curl)
 - [in a serverless app](#test-the-model-in-a-serverless-app)

### Test the model using cURL

Once deployed, you can test the model from the command line. For example:

```
curl -d "{ \"text\": [ \"I would like to punch you.\", \"In hindsight, I do apologize for my previous statement.\" ]}" -X POST "http://localhost:5000/model/predict" -H "Content-Type: application/json"
```

You should see a JSON response like that below:

```json
{
  "status": "ok",
  "predictions": [
    {
      "toxic": 0.9796434044837952,
      "severe_toxic": 0.07256636023521423,
      "obscene": 0.058431386947631836,
      "threat": 0.8635178804397583,
      "insult": 0.11121545732021332,
      "identity_hate": 0.013826466165482998
    },
    {
      "toxic": 0.00029103411361575127,
      "severe_toxic": 0.00012417171092238277,
      "obscene": 0.0001522742968518287,
      "threat": 0.00008440738747594878,
      "insult": 0.00016013195272535086,
      "identity_hate": 0.00012860879360232502
    }
  ]
}
```

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
