## Overview

**Note**: This small subset of the Project CodeNet dataset is intended to showcase a language classification model and only comprises 2198 random samples across 10 languages.

Project CodeNet is a large-scale dataset with approximately 14 million code samples, each of which is an intended solution to one of 4000 coding problems. The code samples are obtained from downloading submissions from two online judge web sites: [AIZU Online Judge](https://judge.u-aizu.ac.jp/onlinejudge/) and [AtCoder](https://atcoder.jp/). The code samples are written in over 50 programming languages (although the dominant languages are C++, C, Python, and Java) and they are annotated with a rich set of information, such as its code size, memory footprint, cpu run time, and status, which indicates acceptance or error types. The dataset is accompanied by a [repository](https://github.com/IBM/Project_CodeNet), where we provide a set of [tools](https://github.com/IBM/Project_CodeNet/tree/main/tools) to aggregate codes samples based on user criteria and to transform code samples into token sequences, simplified parse trees and other code graphs. A detailed discussion of Project CodeNet is available in this [paper](https://arxiv.org/abs/2105.12655).

The rich annotation of Project CodeNet enables research in code search, code completion, code-code translation, and a myriad of other use cases. We also extracted several language specific datasets for benchmarking in Python, Java and C++ to drive innovation in deep learning and machine learning models in code classification and code similarity. To expedite AI for code research using graph neural networks, we also made available the simplified parse tree (SPT) representation of the code samples in the four benchmark datasets. 

## Get this Dataset

| Data Description | Archive Dataset File | Archive SPT File |
| --------  | -------- | -------- |
| Full (Original) Dataset | [Project_CodeNet.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet.tar.gz) | N/A |
| Full Dataset, Metadata Only | [Project_CodeNet_metadata.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_metadata.tar.gz) | N/A |
| Mini Project CodeNet | [Mini_Project_CodeNet.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Mini_Project_CodeNet.tar.gz) | N/A |
| Python benchmark | [Project_CodeNet_Python800.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_Python800.tar.gz) | [Project_CodeNet_Python800_spts.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_Python800_spts.tar.gz) |
| Java benchmark | [Project_CodeNet_Java250.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_Java250.tar.gz) | [Project_CodeNet_Java250_spts.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_Java250_spts.tar.gz) |
| C++ benchmark 1 | [Project_CodeNet_C++1000.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_C++1000.tar.gz) | [Project_CodeNet_C++1000_spts.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_C++1000_spts.tar.gz) |
| C++ benchmark 2 | [Project_CodeNet_C++1400.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_C++1400.tar.gz) | [Project_CodeNet_C++1400_spts.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_C++1400_spts.tar.gz) |
| Sample dataset for language classification | [Project_CodeNet_LangClass.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_LangClass.tar.gz) | N/A |
| Sample dataset for masked language models | [Project_CodeNet_MLM.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Project_CodeNet_MLM.tar.gz) | N/A |

## Dataset Metadata

| Field | Value |
| --------  | -------- |
| Format | C++, Java, Python, other programming languages, csv, text|
| Dataset license | [CDLA Permissive v2.0](https://cdla.dev/permissive-2-0/) |
| Source code license | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |
| Domain  | Solutions to programming problems  |
| Number of code samples | 2198 |
| Size | 397KB |
| Author | Ruchir Puri, David Kung, Geert Janssen, Wei Zhang, Giacomo Domeniconi, Vladmir Zolotov, Julian Dolby, Jie Chen, Mihir Choudhury, Lindsey Decker, Veronika Thost, Luca Buratti, Saurabh Pujar, Ulrich Finkler |
| Dataset Version Update | Version 1 – May 5, 2021<br/> |
| Use Cases |**AI for Code**  Code search, Code completion, Code-Code Translation<br/> |


## Dataset Archive Contents
Click [here](https://github.com/IBM/Project_CodeNet#directory-structure-and-naming-convention) for the full dataset's directory structure and contents. The content of each benchmark dataset and its respective SPT file is described in the [README](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/readme.html).

## Data Glossary and Preview
Click [here](https://github.com/IBM/Project_CodeNet#data) to explore the data glossary and [here](https://github.com/IBM/Project_CodeNet#metadata) for details about the metadata. Small [code samples](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/Mini_Project_CodeNet.tar.gz) with [README](https://dax-cdn.cdn.appdomain.cloud/dax-project-codenet/1.0.0/readme.html) are available for preview.

## Use the Dataset

This dataset is complemented by a collection of data exploration and data 
analysis Python notebooks to help you get started:

### Notebook 1: Project CodeNet Language Classification 

This notebook takes you through the steps of a simple experiment that shows how to create and exercise a Keras model to detect the language of a piece of source code. 

[Get the notebook](https://github.com/CODAIT/project-codenet-notebooks/blob/main/Project_CodeNet_LangClass.ipynb)
[Run the notebook in Colab](https://colab.research.google.com/github/CODAIT/project-codenet-notebooks/blob/main/Project_CodeNet_LangClass.ipynb)

### Notebook 2: A Masked Language Model for Project CodeNet

This experiment investigates whether a popular attention model to construct a masked language model (MLM) can be used for source code instead of natural language sentences. 

[Get the notebook](https://github.com/CODAIT/project-codenet-notebooks/blob/main/Project_CodeNet_MLM.ipynb)
[Run the notebook in Colab](https://colab.research.google.com/github/CODAIT/project-codenet-notebooks/blob/main/Project_CodeNet_MLM.ipynb)


## Citation

```text
  @inproceedings{puri2021codenet,
  author = {Ruchir Puri and David Kung and Geert Janssen and Wei Zhang and Giacomo Domeniconi and Vladmir Zolotov and Julian Dolby and Jie Chen and Mihir Choudhury and Lindsey Decker and Veronika Thost and Luca Buratti and Saurabh Pujar and Ulrich Finkler},
  title = {Project CodeNet: A Large-Scale AI for Code Dataset for Learning a Diversity of Coding Tasks},
  year = {2021},
 }
```
