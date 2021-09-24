# Notebooks

The Jupyter notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. A Jupyter notebook should have a self-contained set of code that can be executed using the Jupyter notebook server runtime.

## Create Notebooks

The Jupyter notebooks on MLX should be a self-contained set of code that can be executed on a vanilla Python 3.6 runtime. Then, the notebooks need to be uploaded to GitHub repository.

To register the notebook, we need to create a specification file in YAML format. The file includes information for MLX to view and run the notebook, such as GitHub source and metadata specifications. The [template](template.yaml) has all the details on how to create a notebook specification file.

The [src](src) directory is for hosting some Notebook example source files on GitHub, but the notebook source can be hosted at any place that can be accessed by HTTP/HTTPS.

## Register Notebooks

1. Click on the "Notebooks" link in left-hand navigation panel
2. Click on "Upload a Notebook"
3. Select a file to upload (Must be `.tar.gz` or `.tgz` format)
    - This will be the compressed `.yaml` notebook specification
4. Enter a name for the notebook; Otherwise a default will be given

## List of Sample Notebooks

* [AIF360 Bias Detection](aif-bias.yaml)
* [ART Detector Model](art-detector.yaml)
* [ART Poisoning Attack](art-poison.yaml)
* [CodeNet Laguage Classification](codenet-lang.yaml)
* [CodeNet MLM](codenet-mlm.yaml)
* [JFK Airport Weather Analysis](JFK-airport.yaml)
* [Qiskit Quantum Machine Learning](qiskit-ml.yaml)
* [Qiskit Neural Network Classifier and Regressor](qiskit-nncr.yaml)
