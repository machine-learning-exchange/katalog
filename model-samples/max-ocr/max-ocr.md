## Overview

This repository contains code to instantiate and deploy an optical character recognition model. This model takes an
image of text as an input and returns the predicted text. This model was trained on 20 samples of 94 characters from 8
different fonts and 4 attributes (regular, bold, italic, bold + italic) for a total of 60,160 training samples. Please
see the paper [An Overview of the Tesseract OCR Engine](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/33418.pdf)
for more detailed information about how this model was trained.


## Model Metadata

| Domain        | Application                   | Industry | Framework  | Training Data          | Input Data Format |
|---------------|-------------------------------|----------|------------|------------------------|-------------------|
| Image & Video | Optical Character Recognition | General  | n/a        | Tesseract Data Files   | Image (PNG/JPG)   |

## References


* _Smith, Ray._ ["An overview of the Tesseract OCR engine."](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/33418.pdf)
    Ninth International Conference on Document Analysis and Recognition (ICDAR 2007). Vol. 2. IEEE, 2007.

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| This repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-OCR/blob/master/LICENSE) |
| Model Code (3rd party) | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [Tesseract OCR Repository](https://github.com/tesseract-ocr/tesseract/blob/master/LICENSE) |
| Test Samples | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [Sample README](https://github.com/IBM/MAX-OCR/blob/master/samples/README.md)


## Options available for deploying this model

* Run with Docker:

  ```
  docker run -it -p 5000:5000 codait/max-ocr
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI in [this tutorial](https://github.ibm.com/IBMCode/Code-Tutorials/blob/e29a33f/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/index.md) and specify `codait/max-ocr` as the image name.

* Deploy on Kuberneters:

  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-OCR/master/max-ocr.yaml
  ```

  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-OCR/blob/master/README.md#run-locally)


### Test the model using cURL

Once deployed, you can test the model from the command line. For example if running locally:

```bash
$ curl -F "image=@samples/quick_start_watson_studio.jpg" -XPOST http://localhost:5000/model/predict
```

```json
{
  "status": "ok",
  "text": [
    [
      "Quick Start with Watson Studio"
    ],
    [
      "Watson Studio is IBM’s hosted notebook service, and you can create",
      "a free account at https://www.ibm.com/cloud/watson-studio/. Other",
      "hosted notebook services can be used to run the notebooks as well,",
      "but Watson Studio offers all of the frameworks and languages that",
      "are used for this book’s examples. Once you have created an account",
      "and logged in, you can begin by creating a project and notebook."
    ]
  ]
}
```

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
