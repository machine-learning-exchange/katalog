# MLX Katalog

MLX Katalog is a project to hold the default content samples to bootstrap Machine Learning Exchange. 

## Pipeline Samples

1. OpenScale: An end to end pipeline that trains a custom Spark pipeline model using IBM Spark service. Then store it along with the correct data schema and subscribe with OpenScale for quality and fairness monitoring.
    * Source Link: https://github.com/kubeflow/pipelines/tree/master/samples/contrib/ibm-samples/openscale

2. Watson ML: A simple end to end pipeline that trains a model on Watson Machine Learning. Then it stores and deploys the trained model as web service on Watson Machine Learning.
    * Source Link: https://github.com/kubeflow/pipelines/tree/master/samples/contrib/ibm-samples/watson
   
## Pipeline Component Samples

You can upload the `.tar.gz` files under [component-samples](component-samples) to the Machine Learning Exchange 
Components page to register a new component.

Sample components: monitor_quality, monitor_fairness, wml_train

## Model Samples

You can upload the `.tar.gz` files under [model-samples](model-samples) to the Machine Learning 
Exchange model page to register a new model.

Sample models: image-completer

## Notebook Pipeline Samples

[Watson-ML-pipeline](notebook-samples/Watson-ML-pipeline/watson-ml-pipeline.ipynb): A simple end to end pipeline that trains a model on Watson Machine Learning. Then it stores and deploys the trained model as web service on Watson Machine Learning.
