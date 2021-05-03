# MLX Katalog

MLX Katalog is a project to hold the default content samples to bootstrap Machine Learning Exchange. 

## Pipeline Samples

1. OpenScale: An end to end pipeline that trains a custom Spark pipeline model using IBM Spark service. Then store it along with the correct data schema and subscribe with OpenScale for quality and fairness monitoring.
    * Source Link: https://github.com/kubeflow/pipelines/tree/master/samples/ibm-samples/openscale

2. Watson ML: A simple end to end pipeline that trains a model on Watson Machine Learning. Then it stores and deploys the trained model as web service on Watson Machine Learning.
    * Source Link: https://github.com/kubeflow/pipelines/tree/master/samples/ibm-samples/watson

3. model-pipeline: Two pipelines that process the model metadata and deploy the model using either regular Kubernetes deployment or Knative configuration with custom routing.
    * Source: [model-pipeline](pipeline-samples/model-pipeline/pipelines)

## Pipeline Component Samples

You can upload the tar.gz files under [component-samples](component-samples) to the Machine Learning Exchange component page to register a new component.

Sample components: monitor_quality, monitor_fairness, wml_train

## Model Samples

You can upload the tar.gz files under [model-metadata-samples](model-metadata-samples) to the Machine Learning Exchange model page to register a new model.

Sample models: image-completer, gender-classification

## Notebook Pipeline Samples

1. [Watson-ML-pipeline](notebook-samples/Watson-ML-pipeline/watson-ml-pipeline.ipynb): A simple end to end pipeline that trains a model on Watson Machine Learning. Then it stores and deploys the trained model as web service on Watson Machine Learning.

2. [watson-openscale](notebook-samples/watson-openscale/watson-openscale.ipynb): An end to end pipeline that trains a custom Spark pipeline model using IBM Spark service. Then store it along with the correct data schema and subscribe with OpenScale for quality and fairness monitoring.

