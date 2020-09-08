# Wavelet Based Deseasonalization Approach for Day Ahead Load Forecast Error Prediction

The purpose of the seminar is to predict the error between the actual energy load and the day-ahead forecast. The energy load used and the day-ahead forecast are from the energy grid Denmark West

This seminar work will aim to identify an underlying seasonal pattern and to extract and model this seasonal pattern. It is assumed that the seasonal component  is deterministic. The seasonal component is then included in the model as an exogenous variable, in order to improve the forecast performance. 

This paper uses the wavelet based decomposition approach to identify possible seasonal patterns in the forecasting error. The idea is to extract the seasonal component from the forecasting error time series and to model it for day-ahead forecast. For simplicity the seasonal component is assumed to be deterministic. The derived error, by regressing the seasonal component on the actual data will be modeled with a SARIMA model. \\
As evaluation for the wavelet based decomposition approach, a basic SARIMA model is fitted on the actual forecasting error without any deseasonalization beforehand. 