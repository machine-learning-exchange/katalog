## Overview

PubTabNet contains heterogeneous tables in both image and HTML format. PubTabNet can be used to train and evaluate image-based table recognition models. The model needs to recognize both the structure and the content of the tables, and be able to reconstruct the HTML representation of the tables solely relying on the table images. The HTML representation encodes both the structure of the tables and the content in each table cell. Position (bounding box) of table cells is also provided to support more diverse model designs. The source of the tables is PubMed Central Open Access Subset (commercial use collection). The tables (in both image and HTML format) are automatically extracted by matching the PDF format and the XML format of the articles in the PubMed Central Open Access Subset.

## Dataset Metadata

| Field | Value |
| --------  | -------- |
| Format | [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)<br/>[JSON](https://json.org)<br/> |
| License | [CDLA-Permissive](https://cdla.io/permissive-1-0/) |
| Domain  | Computer Vision
| Number of Records | 516k+ images |
| Size | 30GB |
| Author | [Xu Zhong](https://researcher.watson.ibm.com/researcher/view.php?person=au1-peter.zhong), [Elaheh ShafieiBavani](https://researcher.watson.ibm.com/researcher/view.php?person=ibm-Elaheh.Shafieibavani), [Antonio Jimeno Yepes](https://researcher.watson.ibm.com/researcher/view.php?person=au1-antonio.jimeno) |
| Dataset Origin | Images of research papers from [PubMed](https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/) and annotations from [IBM Research Australia](https://arxiv.org/abs/1911.10683). |
| Dataset Version Update | Version 2 - July 20, 2020 <br/>Version 1 - November 11, 2019<br/> |
| Data Coverage | The dataset contains images of research papers from the medical domain. |
| Business Use Case | **Document Understanding:** The dataset can be used to train a model to extract various elements of a document such as tables, figures, texts etc. This can aid businesses dealing with a large number of documents to easily categorize the various elements in their documents.<br/>|

## Dataset Archive Contents
| File or Folder | Description |
|-------------|-------------|
| `train` folder | Train data folder |
| `test` folder | Test data folder |
| `val` folder | Validation data folder |
| `PubTabNet_2.0.0.jsonl` | Data glossary of the three folders above. |

## Data Glossary and Preview

Click [here](https://dax-cdn.cdn.appdomain.cloud/dax-pubtabnet/2.0.0/data-preview/index.html) to explore the data glossary, sample records, and additional dataset metadata.

## Use the Dataset

This dataset is complemented by data exploration, data analysis, and modeling Python notebooks to help you get started:
 - [Run the notebooks in Watson Studio](https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/0aa641b0-af25-4470-b9e1-6b33d6b5b66a/view?access_token=b7d5880bb60c253457a72e3ec76f9ab40ccc42c607331acdcbbbe21be4c46bc8&cm_sp=ibmdev-_-developer-exchanges-_-cloudreg)

## Citation

```
@article{zhong2019pubtabnet,
title={Image-based table recognition: data, model, and evaluation},
author={Xu Zhong and Elaheh ShafieiBavani and Antonio Jimeno Yepes},
journal={arXiv preprint arXiv:1911.10683},
year={2019}
}
```

## Related Links
 * __[PubLayNet - largest dataset ever for document layout analysis](https://developer.ibm.com/exchanges/data/all/publaynet/)__  PubLayNet is a large dataset of document images from PubMed Central Open Access Subset. Each document’s layout is annotated with both bounding boxes and polygonal segmentations. While PubTabNet contains the labels for the tabular elements, PubLayNet contains labels for general semantic understanding of a paper.
