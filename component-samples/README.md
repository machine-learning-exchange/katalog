# Components

> A pipeline component is a self-contained set of code that performs one step in the ML workflow (pipeline), such as data preprocessing, data transformation, model training, and so on. A component is analogous to a function, in that it has a name, parameters, return values, and a body.

## Create a Component

Components are made up of two sets of code. Client code talks to api endpoints for submitting the job. Runtime code does the actual job specified for the component.

Components must also include a specification file in YAML format. The file includes information for Kubeflow to run the component, such as metadata and input/output specifications.

The last step is to dockerize the component code.

For an in-depth guide, take a look at their [component specification](https://www.kubeflow.org/docs/pipelines/reference/component-spec/).

## Register Pipeline Components

1. Click on the "Components" link in left-hand navigation panel
2. Click on "Upload a Component"
3. Select a file to upload (Must be tar.gz or tgz format)
    * This will be the compressed `component.yaml` specification
4. Enter a name for the component; Otherwise a default will be given

## Use Components in a Pipeline

Components are composed into a pipeline using the Kubeflow Pipelines SDK.
Refer to the pipeline [documentation](../pipeline-samples/README.md) for usage.

## List of Sample Datasets
* [Generate Dataset Metadata](dax-to-dlf/component.yaml)
* [Create Dataset Volume](dlf/component.yaml)
* [Echo Sample](echo/component.yaml)
* [Create Secret - Kubernetes Cluster](create-secret/component.yaml)
* [Kubernetes Model Deploy](kube-model-deployment/component.yaml)
* [Create Model Config](model-config/component.yaml)
* [Model Fairness Check](https://github.com/Trusted-AI/AIF360/blob/master/mlops/kubeflow/bias_detector_pytorch/component.yaml)
* [Adversarial Robustness Evaluation](https://github.com/Trusted-AI/adversarial-robustness-toolbox/blob/main/utils/mlops/kubeflow/robustness_evaluation_fgsm_pytorch/component.yaml)
