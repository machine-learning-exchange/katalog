## Overview

The Groningen Meaning Bank (GMB) is a dataset of multi-sentence texts, together with annotations for parts-of-speech, named entities, lexical categories and other natural language structural phenomena.

## Dataset Metadata

| Field | Value |
|-------------|-------------|
| Format | [IOB format](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_%28tagging%29) |
| License | [CDLA-Sharing](https://cdla.io/sharing-1-0/) |
| Domain | Natural Language Processing |
| Number of Records | 1,314,115 terms |
| Size | 10 MB |
| Origin | University of Groningen |
| Dataset Version Update | Version 2 - May 14, 2020<br/>Version 1 – December 19, 2019 |
| Data Coverage| The dataset contains only documents authored by Voice of America VOA, together with documents from the MASC dataset and the CIA World Factbook. |
| Business Use Case | **Linguistics:** Can be used to train a model to perform named entity recognition or part-of-speech tagging, as well as to generate new text features. |


## Dataset Archive Contents

| File or Folder | Description |
|-------------|-------------|
| `gmb_subset_full.txt`  | A full version of the raw dataset. Used to train MAX model – Named Entity Tagger. |
| `LICENSE.txt` | Terms of Use |
| `README.txt` | Explains dataset information |

## Data Glossary and Preview
Click [here](https://dax-cdn.cdn.appdomain.cloud/dax-groningen-meaning-bank-modified/1.0.2/data-preview/index.html) to explore the data glossary, sample records, and additional dataset metadata.

## Use the Dataset

This dataset is complemented by data exploration, data visualization, and modeling Python notebooks to help you get started:

 - [Preview the completed notebooks](https://dax-nb-preview-prod.s3.us.cloud-object-storage.appdomain.cloud/preview_notebooks.html?dataset=groningen-meaning-bank)
 - [Run the notebooks in Watson Studio](https://dataplatform.cloud.ibm.com/exchange/public/entry/view/00d1f36477e7a092a43a264d410d5451?cm_sp=ibmdev-_-developer-exchange-_-cloudreg)

Quick access in Python (requires the [`pardata`](https://pardata.readthedocs.io) pypi package):

`$ pip install pardata`

```python
import pardata
data = pardata.load_dataset('gmb')
```

## Citation

```
@incollection{Bos2017GMB,
   title     = {The Groningen Meaning Bank},
   author    = {Bos, Johan and Basile, Valerio and Evang, Kilian and Venhuizen, Noortje and Bjerva, Johannes},
   booktitle = {Handbook of Linguistic Annotation},
   editor    = {Ide, Nancy and Pustejovsky, James},
   publisher = {Springer},
   volume    = {2},
   pages     = {463--496},
   year      = {2017}
}
```

## Related Links

- [Groningen Meaning Bank](https://www.researchgate.net/publication/317902904_The_Groningen_Meaning_Bank)
- [Model Asset Exchange - Named Entity Tagger](https://github.com/IBM/MAX-Named-Entity-Tagger/)
- [Part-of-speech Tags](https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)