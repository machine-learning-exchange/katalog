## Overview

This model annotates each word or term in a piece of text with a tag representing the entity type, taken from a list of 17 entity tags from [The Groningen Meaning Bank (GMB) dataset](http://gmb.let.rug.nl/data.php). These tags cover 8 types of named entities: persons, locations, organizations, geo-political entities, artifacts, events, natural objects, time, as well as a tag for 'no entity' (see the [GMB dataset manual page](http://gmb.let.rug.nl/manual.php) for the full entity definitions). The entity types furthermore may be tagged with either a "B-" tag or "I-" tag. A "B-" tag  indicates the first term of a new entity (or only term of a single-term entity), while subsequent terms in an entity will have an "I-" tag. For example, "New York" would be tagged as `["B-GEO", "I-GEO"]` while  "London" would be tagged as `"B-GEO"`.

The model consists of a recurrent neural network architecture with a bidirectional LSTM layer applied to character-level embedding vectors, which are combined with pre-trained [GloVe 6B](https://nlp.stanford.edu/projects/glove/) word vector embeddings; finally a second bidirectional LSTM layer is applied to this combined vector representation. The input to the model is a string and the output is a list of terms in the input text (after applying simple tokenization), together with a list of predicted entity tags for each term.

The model is based on Guillaume Genthial's [Named Entity Recognition with TensorFlow model](https://github.com/guillaumegenthial/sequence_tagging), adapted to use the Keras framework. The model was trained on a subset of the GMB dataset version `2.2.0` by the [IBM CODAIT team](https://medium.com/codait).

## Model Metadata
| Domain | Application | Industry  | Framework | Training Data | Input Data Format |
| ------------- | --------  | -------- | --------- | --------- | -------------- |
| Natural Language Processing | Named Entity Recognition | General | Keras | [Groningen Meaning Bank (GMB) Dataset](http://gmb.let.rug.nl/data.php) | Text |

*Note* the underlying dataset is primarily based on news articles and so the model should perform relatively better on input related to general news, business, geo-political and sporting events. The dataset covers a period up until 2014, which governs the entities the model will be aware of.

## References

* _G. Lample, M. Ballesteros, S. Subramanian, K. Kawakami, C. Dyer_, ["Neural Architectures for Named Entity Recognition"](https://arxiv.org/pdf/1603.01360), arXiv, 2016.
* _X. Ma and E. Hovy_, ["End-to-end Sequence Labeling via Bi-directional LSTM-CNNs-CRF"](https://arxiv.org/pdf/1603.01354.pdf), arXiv, 2016.
* [Named Entity Recognition with TensorFlow.](https://github.com/guillaumegenthial/sequence_tagging)
* _V. Basile, J. Bos, K. Evang, N. Venhuizen_, ["Developing a large semantically annotated corpus"](http://www.let.rug.nl/bos/pubs/BasileBosEvangVenhuizen2012LREC.pdf), in Proceedings of the
 Eighth International Conference on Language Resources and Evaluation (LREC-2012), pages 3196-3200. European Language Resources Association (ELRA). 2012.
* [GMB dataset about page](http://gmb.let.rug.nl/about.php) and [dataset manual](http://gmb.let.rug.nl/manual.php).
* [stokastik blog resources GitHub repository](https://github.com/funktor/stokastik/blob/master/NER/NER.py).

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| Model Repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Named-Entity-Tagger/blob/master/LICENSE) |
| Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Named-Entity-Tagger/blob/master/LICENSE) |
| Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [TensorFlow NER Repo License](https://github.com/guillaumegenthial/sequence_tagging/blob/master/LICENSE.txt) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Deploy from Dockerhub:

  ```
  docker run -it -p 5000:5000 codait/max-named-entity-tagger
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://developer.ibm.com/tutorials/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/) and specify `codait/max-named-entity-tagger` as the image name.

* Deploy on Kubernetes:

  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Named-Entity-Tagger/master/max-named-entity-tagger.yaml
  ```

  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Named-Entity-Tagger#run-locally)

## Example Usage

You can test or use this model
 - [using cURL](#test-the-model-using-curl)
 - [in a serverless app](#test-the-model-in-a-serverless-app)


### Test the model using cURL

Once deployed, you can test the model from the command line. For example:

```
curl -X POST -H 'Content-Type: application/json' -d '{"text":"John lives in Brussels and works for the EU"}' 'http://localhost:5000/model/predict'
```

You should see a JSON response like that below:

```json
{
    "status": "ok",
    "prediction": {
        "entities": [
            "B-PER",
            "O",
            "O",
            "B-GEO",
            "O",
            "O",
            "O",
            "O",
            "B-ORG"
        ],
        "input_terms": [
            "John",
            "lives",
            "in",
            "Brussels",
            "and",
            "works",
            "for",
            "the",
            "EU"
        ]
    }
}
```

### Test the model in a serverless app

You can utilize this model in a serverless application by following the instructions in the [Leverage deep learning in IBM Cloud Functions](https://developer.ibm.com/tutorials/leverage-deep-learning-in-apache-openwhisk-ibm-cloud-functions/) tutorial.


## Options available for training this model

This model can be trained using the following mechanisms:

* Train on IBM Cloud - Watson Machine Learning: follow the instructions in the [model training README on GitHub](https://github.com/IBM/MAX-Named-Entity-Tagger/tree/master/training).

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
