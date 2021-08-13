---
# Front matter (metadata).
authors:    # REQUIRED - Original authors of the dataset (not CODAIT) and link to their website. Note: can be one or more
  - name: "NOAA"
    url: "https://www.ncdc.noaa.gov"
    email: ""

completed_date: "2019-07-16"    # REQUIRED - Publish date of dataset on DAX. Note: date format is YYYY-MM-DD.

components:
# For a full list of options see https://github.ibm.com/IBMCode/Definitions/blob/master/components.yml
# Use the "slug" value found at the link above to include it in this content.
 - "data-asset-exchange"

# This is to put the model assets into developer.ibm.com/collections/codait
# Don't change this field normally
collections:
  - "codait"

# NOTE - here we use the 'demo' field to represent the primary button for "Get this dataset". It's a bit of a hack for now!
# Ideally to be replaced by dedicated 'dataset_url' field
demo:
  - type: demo    # REQUIRED - Link to download the dataset
    url_or_id: '#get-this-dataset' # Take users to "get this dataset" section
    sha512sum: "e3f27a8fcc0db5289df356e3f48aef6df56236798d5b3ae3889d358489ec6609d2d797e4c4932b86016d2ce4a379ac0a0749b6fb2c293ebae4e585ea1c8422ac"
    button_title: "Get this dataset"
  # Examples of other common buttons
  # OPTIONAL - Note: Alternate links to be displayed in addition to `dataset_url`. These links will create buttons that appear below "Get this dataset",
  #                  in the order they appear in this list, with the button titles that appear in this list.
  #                  The "type" field is for future use and should be kept consistent across datasets
  - type: demo
    url_or_id: "https://dataplatform.cloud.ibm.com/exchange/public/entry/view/a7432f0c29c5bda2fb42749f363bd9ff?cm_sp=ibmdev-_-developer-exchanges-_-cloudreg"
    button_title: "Run dataset notebooks"
  - type: demo
    url_or_id: "https://dax-cdn.cdn.appdomain.cloud/dax-noaa-weather-data-jfk-airport/1.1.4/data-preview/index.html"
    button_title: "Preview the data & notebooks"
  # - type: demo
  #   url_or_id:
  #   button_title: "Try the demo"
  # - type: demo
  #   url_or_id:
  #   button_title: "View the model"

draft: false   # REQUIRED

ignore_prod: false   # OPTIONAL; if true the latest version of this page is only displayed in the staging environment

excerpt: "Local climatological data originally collected at JFK airport."    # REQUIRED - Dataset 'short description'; used on the Dataset tile.

subtitle: "Local climatological data originally collected at JFK airport."   # REQUIRED - duplicates 'excerpt'

keywords: "open source, artificial intelligence"    # REQUIRED - This is a comma separated list of keywords used for SEO purposes.

last_updated: "2020-08-11"    # REQUIRED - Note: date format is YYYY-MM-DD. Manually updated.
                                      # Must be changed only on significant changes in content in index.md or underlying dataset (e.g. new version published)

title: "NOAA Weather Data - JFK Airport"   # REQUIRED - Dataset title. This should be descriptive and concise.

primary_tag: "artificial-intelligence"    # REQUIRED - This is needed or the publishing pipeline wont pick up the dataset

pta:    # REQUIRED - Note: can be only one. Almost always will be "cognitive, data, and analytics" for DAX datasets
# For a full list of options see https://github.ibm.com/IBMCode/Definitions/blob/master/primary-technology-area.yml
# Use the "slug" value found at the link above to include it in this content.
 - "cognitive, data, and analytics"

pwg:    # REQUIRED - Note: can be one or many. Typically will be 'analytics' for DAX datasets
# For a full list of options see https://github.ibm.com/IBMCode/Definitions/blob/master/portfolio-working-group.yml
# Use the "slug" value found at the link above to include it in this content.
 - "analytics"

#related_content:   # OPTIONAL - Note: zero or more related content. Used for IBM Code content that is related to the dataset.
#  - type: pattern|article|tutorial|video|presentation
#    slug:

related_links:    # OPTIONAL - Note: zero or more related links
  - title: "Data Asset eXchange (DAX)"
    url: "https://developer.ibm.com/exchanges/data/"
    description: "Explore useful and relevant data sets for enterprise data science."

  - title: "Model Asset eXchange (MAX)"
    url: "https://developer.ibm.com/exchanges/models/"
    description: "A place for developers to find and use free and open source deep learning models."

  - title: "Center for Open-Source Data & AI Technologies (CODAIT)"
    url: "http://codait.org"
    description: "Improving the Enterprise AI Lifecycle in Open Source."

tags:   # OPTIONAL - Note: for DAX datasets this tag field will typically be used for tagging industry or AI application (if a relevant tag exists in the list)
# Please select tags from the complete set of tags below. Do not create new tags. Only use tags specifically targeted for your content. If your content could match all tags (for example cloud, hybrid, and on-prem) then do not tag it with those tags. Less is more.
# For a full list of options see https://github.ibm.com/IBMCode/Definitions/blob/master/tags.yml
# Use the "slug" value found at the link above to include it in this content.
  - "codait"             # This will put the dataset into tracking in DEG Analytics Dashboard

dataset_tags:             # REQUIRED. General data type and/or applicable broad use case for the dataset.
# For example, 'Time Series' or 'Natural Language Processing'. Can have multiple values.
# For a full list of options see https://github.ibm.com/IBMCode/Code-Data-Technologies
# Use the "slug" value - which is the directory name for the relevant tag in the above repo - to include it in this content.
 - time_series_data_model
 - weather_data_model

dataset_primary_tag: "time_series_data_model"      # REQUIRED. The primary 'dataset_tag' off which dataset landing page image is based. Must be one of the values in 'dataset_tags'.

dataset_version:           # REQUIRED. Version of the dataset
  - "1.1.2"

# This is for display on the tile & header section of dataset page
dataset_license:         # REQUIRED. License the dataset uses
  - title: "CDLA-Sharing"
    url: "https://cdla.io/sharing-1-0/"

# This is for display on the tile & header section of dataset page
dataset_format:            # REQUIRED. Data format of the dataset - can be multiple values
 - "CSV"

---
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

* __[MAX Weather Forecaster](https://developer.ibm.com/exchanges/models/all/max-weather-forecaster/)__ link to our MAX weather forecasting model trained using the cleaned data provided in this archive
* __[NOAA LCD Data Download Platform](https://www.ncdc.noaa.gov/cdo-web/datatools/lcd)__ website where you can choose new geographic locations for which to download local weather data from
* __[NOAA LCD JFK Weather Station](https://www.ncdc.noaa.gov/cdo-web/datasets/LCD/stations/WBAN:94789/detail)__ website with JFK Local Climatological Data station details
* __[NOAA LCD Data Documentation](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/LCD_documentation.pdf)__ document that provides NOAA LCD data dictionary

<script defer type='text/javascript' src='/developerapi/offers/burbidge.js'></script>