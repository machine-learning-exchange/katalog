## Overview

Text Clustering can be applied to texts at different levels, from single words to full documents, and can vary with respect to the clustering goal. In thematic clustering, the aim is to cluster texts based on thematic similarity between them, namely grouping together texts that discuss the same theme. In this dataset "Thematic Clustering of Sentences" sentences are annotated for their thematic clusters.

## Dataset Metadata

| Field | Value |
|-------------|-------------|
| Format | [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) |
| License | [CC-BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) |
| Domain | Natural Language Processing |
| Number of Records | 692 articles |
| Data Split | N/A |
| Size | 10.6 MB |
| Author | Ein-Dor, Liat and Mass, Yosi and Halfon, Alon and Venezian, Elad and Shnayderman, Ilya and Aharonov, Ranit and Slonim, Noam |
| Dataset Origin | [IBM Research - Project Debater](https://www.research.ibm.com/artificial-intelligence/project-debater/) |
| Dataset Version Update | Version 1.0.2 - 2018-10-27 |
| Data Coverage| The dataset contains 692 articles from Wikipedia, where the number of sections(clusters) in each article ranges from 5 to 12, and the number of sentences per article ranges from 17 to 1614. |
| Business Use Case | **Document Understanding** Thematic clustering of sentences is important for various use cases. For example, in multi-document summarization, one often extracts sentences from multiple documents that should be organized into meaningful sections and paragraphs. Similarly, within the emerging field of computational argumentation, arguments may be found in a widespread set of articles, which further require thematic organization to generate a compelling argumentative narrative |

## Dataset Archive Contents

| File or Folder | Description |
|-------------|-------------|
| `dataset.csv` | Contains all their sentences and thematic clusters |
| `LICENSE.txt` | Terms of Use |
| `README.txt` | Description of files and the data |

## Data Glossary and Preview

Click [here](https://dax-cdn.cdn.appdomain.cloud/dax-thematic-clustering-of-sentences/1.0.2/data_preview/index.html) to explore the data glossary, sample records, and additional dataset metadata.

## Use the Dataset

This dataset is complemented by a data exploration Python notebook to help you get started:

 - [Run the notebook in Watson Studio](https://dataplatform.cloud.ibm.com/exchange/public/entry/view/cf94e708b8f4b058e8a932eddc217832?cm_sp=ibmdev-_-developer-exchanges-_-cloudreg)

Quick access in Python (requires the [`pardata`](https://pardata.readthedocs.io) pypi package):

`$ pip install pardata`

```python
import pardata
data = pardata.load_dataset('thematic_clustering_of_sentences')
```

## Related Links

- __[Project Debater](https://www.research.ibm.com/artificial-intelligence/project-debater/)__ Project Debater is the first AI system that can debate humans on complex topics. The goal is to help people build persuasive arguments and make well-informed decisions. This dataset contributed to training the models in Project Debater.

## Citation

```bibtex
@inproceedings{dor2018learning,
title={Learning Thematic Similarity Metric from Article Sections Using Triplet Networks},
author={Ein-Dor, Liat and Mass, Yosi and Halfon, Alon and Venezian, Elad and Shnayderman, Ilya and Aharonov, Ranit and Slonim, Noam},
booktitle={Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)},
pages={49--54},
year={2018}
}
```
