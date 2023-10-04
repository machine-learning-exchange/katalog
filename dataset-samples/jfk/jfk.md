## Overview

The NOAA JFK dataset contains 114,546 hourly observations of various local climatological variables (including visibility, temperature, wind speed and direction, humidity, dew point, and pressure). The data was collected by a NOAA weather station located at the John F. Kennedy International Airport in Queens, New York.

## Get this Dataset
| Data Description | Zipped File Name |
| --------  | -------- |
| Full (Original) Dataset, 3.5 MB | [noaa-weather-data-jfk-airport.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-data-jfk-airport.tar.gz) |
| Sample Dataset, 80 KB | [noaa-weather-sample-data.tar.gz](https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/noaa-weather-sample-data.tar.gz)  |

## Dataset Metadata

| Field | Value |
| --------  | -------- |
| Format | [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)<br/> |
| License | [CDLA-Sharing](https://cdla.io/sharing-1-0/) |
| Domain  | Time Series
| Number of Records | 114,546 hourly observations<br/> |
| Data Split | NA |
| Size | 3.2 MB |
| Dataset Origin | [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov/) |
| Dataset Version Update | Version 2 – September 12, 2019<br/>Version 1 – July 16, 2019<br/> |
| Data Coverage | **Location:** New York City<br/>**Dates:** 2010-01-01 through 2018-07-27<br/>**Note:** To download raw data from NOAA for a different region or date span, follow the steps outlined in the data archive's `README.txt`. |
| Business Use Case | **Agriculture:** Detect unseasonal temperature change and alert farmers about potential damage to plants.<br/>**Construction:** Integrate hourly temperature into building model simulations to test structural integrity.<br/> |

## Dataset Archive Contents

| File or Folder            | Description                                                                  |
| ------------------------- | ---------------------------------------------------------------------------- |
| `jfk_weather.csv`         | Raw data obtained directly from NOAA.                                        |
| `jfk_weather_cleaned.csv` | Cleaned version of the raw dataset. Used to train MAX model.                 |
| `LICENSE.txt`             | Terms of Use                                                                 |
| `clean_data.py`           | Script used to generate `jfk_weather_cleaned.csv`                            |
| `README.txt`              | Explains dataset information and steps for extracting similar data from NOAA |

## Data Glossary and Preview

Click [here](https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/data-preview/index.html) to explore the data glossary, sample records, and additional dataset metadata.

## Use the Dataset

This dataset is complemented by data exploration, data analysis, and modeling Python notebooks to help you get started:
 - [Run the notebooks in Watson Studio](https://dataplatform.cloud.ibm.com/exchange/public/entry/view/a7432f0c29c5bda2fb42749f363bd9ff?cm_sp=ibmdev-_-developer-exchanges-_-cloudreg)
 - [Run the notebooks as a pipeline using the Elyra extension for JupyterLab](https://github.com/elyra-ai/examples/tree/master/pipelines/dax_noaa_weather_data)

Quick access in Python (requires the [`pardata`](https://pardata.readthedocs.io) pypi package):

`$ pip install pardata`


```python
import pardata
data = pardata.load_dataset('noaa_jfk')
```

## Related Links

* __[MAX Weather Forecaster](https://github.com/IBM/MAX-Weather-Forecaster/)__ link to our MAX weather forecasting model trained using the cleaned data provided in this archive
* __[NOAA LCD Data Download Platform](https://www.ncdc.noaa.gov/cdo-web/datatools/lcd)__ website where you can choose new geographic locations for which to download local weather data from
* __[NOAA LCD JFK Weather Station](https://www.ncdc.noaa.gov/cdo-web/datasets/LCD/stations/WBAN:94789/detail)__ website with JFK Local Climatological Data station details
* __[NOAA LCD Data Documentation](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/LCD_documentation.pdf)__ document that provides NOAA LCD data dictionary
