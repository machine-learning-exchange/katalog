## Overview

TensorFlow Speech Command dataset is a set of one-second .wav audio files, each containing a single spoken English word. These words are from a small set of commands, and are spoken by a variety of different speakers. 20 of the words are core words, while 10 words are auxiliary words that could act as tests for algorithms in ignoring speeches that do not contain triggers. Included along with the 30 words is a collection of background noise audio files. The dataset was originally designed for limited vocabulary speech recognition tasks. The audio clips were originally collected by Google, and recorded by volunteers in uncontrolled locations around the world.

## Dataset Metadata

| Field | Value |
| ----- | ----- |
| Format | [WAV](https://en.wikipedia.org/wiki/WAV) |
| License | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| Domain  | Audio |
| Number of Records | 65,000 WAV files |
| Data Split | Train - 51,094 audio clips, Validation - 6,798 audio clips, Test - 6,835 audio clips |
| Size | 1.49 GB |
| Dataset Origin | The audio clips were originally collected by [Google](https://ai.googleblog.com/2017/08/launching-speech-commands-dataset.html). <br/><br/> [Recorded](https://github.com/petewarden/extract_loudest_section) by volunteers in uncontrolled locations around the world. |
| Dataset Version | Version 1 – March 17, 2020 |
| Data Coverage | **Core words:** Yes, No, Up, Down, Left, Right, On, Off, Stop, Go, Zero, One, Two, Three, Four, Five, Six, Seven, Eight, and Nine. <br/> <br/>**Auxiliary words:** Bed, Bird, Cat, Dog, Happy, House, Marvin, Sheila, Tree, and Wow.<br/> <br/> **Background noise:** doing_the_dishes, dude_miaowing, exercise_bike, pink_noise, running_tap, and white_noise.<br/> <br/>To know more about the data collection process go through data archive's `README.md`. |
| Business Use Case | Build voice recognition systems that are widely used in the Internet of Things, Automotive, Security and UX/UI.<br/> <br/>Build voice based search applications and voice-activated assistants.<br/><br/> |

## Dataset Archive Contents

| File or Folder    | Description    |
| ----------------- | ---------------|
| `31 Audio clip folders`         | Folders containing audio clips |
| `testing_list.txt` | Path to all the files in the test set.|
| `validation_list.txt`| Path to all the files in the validation set.|
| `LICENSE.txt`             | Terms of Use   |
| `README.md`               | Explains data collection, processing details, and steps for splitting dataset |

## Data Glossary and Preview

Click [here](https://dax-cdn.cdn.appdomain.cloud/dax-tensorflow-speech-commands/1.0.1/data_preview/index.html) to explore the data glossary, sample records, and additional dataset metadata.

## Use the Dataset

This dataset is complemented by starter notebooks that will help you get started:

 - [Preview the completed notebooks](https://dax-nb-preview-prod.s3.us.cloud-object-storage.appdomain.cloud/preview_notebooks.html?dataset=speech-commands)
 - [Run the notebooks in Watson Studio](https://dataplatform.cloud.ibm.com/exchange/public/entry/view/e20607d75c8473daaade1e77c22486ff?cm_sp=ibmdev-_-developer-exchanges-_-cloudreg)

Quick access in Python (requires the [`pardata`](https://pardata.readthedocs.io) pypi package):

`$ pip install pardata`


```python
import pardata
data = pardata.load_dataset('tensorflow_speech_commands')
```

## Related Links

* __[Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition](https://arxiv.org/abs/1804.03209)__ Describes how the data was collected and verified, what it contains, previous versions and properties.

## Citation

```
@article{speechcommands, title={Speech Commands: A public dataset for
single-word speech recognition.}, author={Warden, Pete}, journal={Dataset
available from
http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz}, year={2017}
}
```
