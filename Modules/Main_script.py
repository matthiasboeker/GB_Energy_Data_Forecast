#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:42:23 2019

@author: matthiasboeker
Main Script """
import pandas as pd
import numpy as np
import pywt
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller,kpss
import statsmodels.api as sm
import modwt

#Generate Out-of Sample Train and Test Series 
train_16, test_16 , train_size_16 = interval_test_train_split(dat_series_16 ,interval=96*4)
train_17, test_17 , train_size_17 = interval_test_train_split(dat_series_17 ,interval=96*4)
train_18, test_18 , train_size_18 = interval_test_train_split(dat_series_18 ,interval=96*4)


#Fit a model to the seasonal component in Fitting_Seasonal_Comp.py
mean_w_16
mean_w_17
mean_w_18
wvtrans_mean = pd.DataFrame(wvtrans_mean)


#Deseasonalize Day-ahead Forecasting Error
#Choose which seasonal form is assumed 
#Additive or multiplicative Seasonality 

wvtrans_mean.index = dat_series_16.index
add_deseason_16 = dat_series_16['Forecasting Error'] - wvtrans_mean[0]




#Additive Model  16
tot_wvtrans_16.index = dat_series_16.index
add_deseason_16 = dat_series_16['Forecasting Error'] - wvtrans_mean[0]

#Additive Model  17
mean_w_17.index = dat_series_17.index
add_deseason_17 = dat_series_17['Forecasting Error'] - mean_w_17[0]

#Additive Model  18
mean_w_18.index = dat_series_18.index
add_deseason_18 = dat_series_18['Forecasting Error'] - mean_w_18[0]

#Multiplicative Model 
wvtrans.index = train_main_series.index
mulp_deseason = np.log(train_main_series['Forecasting Error'])- np.log(wvtrans)


#Forecast deseasonalized residual model with ARIMA in ARIMA_Resiudals.py

#Add seasonal component back to the residuals 
#Merge residual model with its prediction
x = add_deseason_16[:train_size_16]
des_full_16 = x.append(predictions_exog1.predicted_mean,ignore_index=True)


# Add deseasonalized series to transformed 
plt.plot(back_transform)
plt.plot(wvtrans_mean)
plt.plot(x)

x.index = wvtrans_mean[:train_size_16+96].index
back_transform = wvtrans_mean[:train_size_16+96]+des_full_16[0]
back_transform.index = dat_series_16[:train_size_16+96].index
evaluate_prediction(dat_series_16['Total Load'][train_size_16:train_size_16+96],back_transform[train_size_16:train_size_16+96])

plt.plot(dat_series_16['Total Load'][train_size_16:train_size_16+96])
plt.plot(back_transform[train_size_16:train_size_16+96])

