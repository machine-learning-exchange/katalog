## Overview

This model takes hourly weather data (as a Numpy array of various weather features, in text file format) as input and returns hourly weather predictions for a specific target variable or variables (such as temperature or windspeed).

Three pre-trained models are provided, all trained by the [CODAIT team](https://developer.ibm.com/open/centers/codait/) on [National Oceanic and Atmospheric Administration](https://www.ncdc.noaa.gov) local climatological data originally collected by JFK airport. All three models use an LSTM recurrent neural network architecture.

A description of the weather variables used to train the models is set out below.

| Variable                 | Description           |
|---------------          | ----------------------|
| HOURLYVISIBILITY        | Distance from which an object can be seen. |
| HOURLYDRYBULBTEMPF      | Dry bulb temperature (degrees Fahrenheit). Most commonly reported standard temperature. |
| HOURLYWETBULBTEMPF      | Wet bulb temperature (degrees Fahrenheit).  |
| HOURLYDewPointTempF     | Dew point temperature (degrees Fahrenheit). |
| HOURLYRelativeHumidity  | Relative humidity (percent). |
| HOURLYWindSpeed         | Wind speed (miles per hour). |
| HOURLYStationPressure   | Atmospheric pressure (inches of Mercury; or 'in Hg'). |
| HOURLYSeaLevelPressure  | Sea level pressure (in Hg). |
| HOURLYPrecip            | Total precipitation in the past hour (in inches). |
| HOURLYAltimeterSetting  | Atmospheric pressure reduced to sea level using temperature profile of the “standard” atmosphere (in Hg). |
| HOURLYWindDirectionSin     | Sine component of wind direction transformation (since wind direction is cyclical). |
| HOURLYWindDirectionCos     | Cosine component of wind direction transformation (since wind direction is cyclical). |
| HOURLYPressureTendencyIncr  | Dummy variable indicating if pressure was increasing in the past hour. |
| HOURLYPressureTendencyDecr  | Dummy variable indicating if pressure was decreasing in the past hour. |
| HOURLYPressureTendencyCons  | Dummy variable indicating if pressure has stayed relatively constant in the past hour. |

For further details on the weather variables see the [US Local Climatological Data Documentation](https://www1.ncdc.noaa.gov/pub/data/cdo/documentation/LCD_documentation.pdf)

Each model returns a different format for its predictions:
* *Univariate Model*: returns a prediction of dry bulb temperature (`HOURLYDRYBULBTEMPF`), for the next hourly time step, for each input data point
* *Multivariate Model*: returns predictions for all 15 weather variables, for the next hourly time step, for each input data point
* *Multistep Model*: returns predictions of dry bulb temperature (`HOURLYDRYBULBTEMPF`), for the next 48 hourly time steps, for each input data point

## Model Metadata

| Domain        | Application           | Industry       | Framework  | Training Data           | Input Data Format |
|---------------|-----------------------|----------------|------------|-------------------------|-------------------|
| Weather       | Time Series Prediction | General | TensorFlow / Keras | [JFK Airport Weather Data, NOAA](https://www.ncdc.noaa.gov/cdo-web/datasets/LCD/stations/WBAN:94789/detail) | CSV |

* Data from [US Local Climatological Data](https://www.ncdc.noaa.gov/cdo-web/datatools/lcd), National Climatic Data Center, National Oceanic & Atmospheric Administration

## References

Literature and Documentation
* [LSTMs in Keras](https://keras.io/layers/recurrent/#lstm)
* [Time Series Prediction with RNNs](https://www.tensorflow.org/tutorials/structured_data/time_series)
* _S. Hochreiter, J. Schmidhuber_ ["Long Short Term Memory"](http://www.bioinf.jku.at/publications/older/2604.pdf), Neural Computation 1997

Related Repositories
* [TensorFlow Tutorials for Time Series](https://github.com/tgjeon/TensorFlow-Tutorials-for-Time-Series)
* [Tensorflow LSTM Regression](https://github.com/mouradmourafiq/tensorflow-lstm-regression)

## Licenses

| Component | License | Link  |
| ------------- | --------  | -------- |
| Model GitHub Repository | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Weather-Forecaster/blob/master/LICENSE) |
| Model Weights | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) | [LICENSE](https://github.com/IBM/MAX-Weather-Forecaster/blob/master/LICENSE) |
| Test Assets | No restriction | [Asset README](https://github.com/IBM/MAX-Weather-Forecaster/blob/master/assets/README.md) |

## Options available for deploying this model

This model can be deployed using the following mechanisms:

* Run with Docker:
  ```
  docker run -it -p 5000:5000 codait/max-weather-forecaster
  ```

* Deploy on Red Hat OpenShift:

  Follow the instructions for the OpenShift web console or the OpenShift Container Platform CLI
  in [this tutorial](https://github.ibm.com/IBMCode/Code-Tutorials/blob/e29a33f/deploy-a-model-asset-exchange-microservice-on-red-hat-openshift/index.md)
  and specify `codait/max-weather-forecaster` as the image name.

* Deploy on Kubernetes:
  ```
  kubectl apply -f https://raw.githubusercontent.com/IBM/MAX-Weather-Forecaster/master/max-weather-forecaster.yaml
  ```

  A more elaborate tutorial on how to deploy this MAX model to production on [IBM Cloud](https://ibm.biz/Bdz2XM) can be found [here](http://ibm.biz/max-to-ibm-cloud-tutorial).

* Locally: follow the instructions in the [model README on GitHub](https://github.com/IBM/MAX-Weather-Forecaster#run-locally)

## Example Usage

Once deployed, you can test the model from the command line. For example to test the multi-step model when running locally:
```
curl -F "file=@assets/lstm_weather_test_data/multistep_model_test_data.txt" -XPOST http://localhost:5000/model/predict?model=multistep
```

You should see a JSON response like that below for the `multistep` test data, where `predictions` contains the predicted dry bulb temperature (in F) for each of the next 48 hours, for each input data point.

```
{
  "status": "ok",
  "predictions": [
    [
      77.51201432943344,
      76.51381462812424,
      75.0168582201004,
      73.84445126354694,
      72.79087746143341,
      71.71804094314575,
      70.97693882882595,
      70.44060184061527,
      69.89843893051147,
      69.35454525053501,
      69.04163710772991,
      68.70432360470295,
      68.37075608968735,
      68.20421539247036,
      68.01852786540985,
      67.6653740555048,
      67.27566187083721,
      67.0398361980915,
      66.69407051801682,
      66.9289058893919,
      67.19844545423985,
      67.65162572264671,
      68.30480472743511,
      69.37090930342674,
      70.37226051092148,
      71.57235226035118,
      72.68855434656143,
      73.91224025189877,
      74.65138283371925,
      75.09161844849586,
      75.30447003245354,
      75.04770956933498,
      74.93723678588867,
      74.27759975194931,
      73.82458955049515,
      73.32358133792877,
      72.66812674701214,
      71.75925283133984,
      71.28871068358421,
      70.66486597061157,
      70.06835387647152,
      69.74887031316757,
      69.49707941710949,
      69.26406812667847,
      68.87126012146473,
      68.60496838390827,
      68.39429907500744,
      68.03596951067448
    ],
    ...
}
```

## Resources and Contributions

If you are interested in contributing to the Model Asset Exchange project or have any queries, please follow the instructions [here](https://github.com/CODAIT/max-central-repo).
