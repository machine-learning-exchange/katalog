## Overview

FinProp 1.0 was developed by researchers at IBM Almaden Research Center, San Jose, CA, USA. FinProp consists of proposition bank-style annotations from approximately 1000 English compliance sentences obtained from IBM’s publicly available annual financial reports. These sentences were extracted from report sections such as “Management’s Discussion and Analysis of Financial Condition and Results of Operations” and “Quantitative and Qualitative Disclosures About Market Risk”. Each of the sentences are annotated with a layer of “universal” semantic role labels covering parts of speech, argument labeling, and predicate labeling. This dataset makes for great training data to train a deep neural network to perform Semantic Role Labeling (SRL) on unlabeled finance domain language. Semantic Role Labeling (SRL) is a process in natural language processing that deals with structurally representing the meaning of a sentence.

## Dataset Metadata

| Field | Value |
|-------------|-------------|
| Format | [CoNLL-U](https://universaldependencies.org/format.html) |
| License | [CDLA-Sharing](https://cdla.io/sharing-1-0/) |
| Domain | Natural Language Processing |
| Number of Records | ~1,000 annotated sentences corresponding to ~50,000 words |
| Size | 2.9 MB |
| Author | Sanjana Sahayaraj, Dulce Ponceleon, [Huaiyu Zhu](https://researcher.watson.ibm.com/researcher/view.php?person=us-huaiyu), [Yunyao Li](https://researcher.watson.ibm.com/researcher/view.php?person=us-yunyaoli), [Marina Danilevsky](https://researcher.watson.ibm.com/researcher/view.php?person=us-mdanile), [Rajasekar Krishnamurthy](https://researcher.watson.ibm.com/researcher/view.php?person=us-rajase) |
| Dataset Origin | IBM Research |
| Dataset Version Update | Version 1 - September 12, 2019 |
| Data Coverage| This dataset contains labeled sentences from IBM’s publicly available annual financial reports. |
| Business Use Case | **Linguistics:** Train a semantic role labeler to provide input for a chatbot model. |

## Dataset Archive Contents

| File or Folder | Description |
|-------------|-------------|
| `finance_proposition_bank.conllx` | A full version of the raw dataset. |
| `LICENSE.txt` | Terms of Use |

## Data Glossary and Preview
Click [here](https://dax-cdn.cdn.appdomain.cloud/dax-finance-proposition-bank/1.0.2/data-preview/index.html) to explore the data glossary, sample records, and additional dataset metadata.

## Use the Dataset

This dataset is complemented by a data exploration Python notebook to help you get started:

 - [Run the notebook in Watson Studio](https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/0e615c46-5e4c-496f-9374-25dde48b46d0/view?access_token=aa16e0d5e3447e3979158b5f5c7de5436b3381424311470ded1686d90835da1e&cm_sp=ibmdev-_-developer-exchanges-_-cloudreg)

## Citation

```
[1] Wen-Chi  Chou,  Richard  Tzong-Han  Tsai,  Ying-ShanSu,  Wei  Ku,  Ting-Yi  Sung,  and  Wen-Lian  Hsu. 2006.   A  semi-automatic  method  for  annotating a biomedical  proposition  bank. In Proceedings of the workshop on frontiers in linguistically annotated corpora 2006. Association for Computational Linguistics, pages 5–12.
[2] Alan  Akbik  and  Yunyao  Li.  2016.    K-srl:   Instance-based learning for semantic role labeling.   In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: Technical Papers. pages 599–608.
[3] Yuta Tsuboi, Hiroshi Kanayama, Katsumasa Yoshikawa, Tetsuya Nasukawa, Akihiro Nakayama, Kei Sugano, John Richardson. 2014. Transfer of dependency parser from rule-based system to learning-based system, Proceedings of 20th Annual Meeting of the Association of Natural Language Processing (in Japanese), 2014.
```
