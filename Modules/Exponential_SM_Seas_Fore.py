#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 12:42:23 2019

@author: matthiasboeker
Main Script """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller,kpss
import statsmodels.api as sm


#Split up the Data into Train and Test
train_main_series, test_main_series , train_main_size = interval_test_train_split(dat_series_18,96)


#Wavelet Transform and Backtransform and extract the seasonal component 
wvtrans = wavelet_signal_select(train_main_series['Forecasting Error'], wavelet='db7', levels= 5, plot=False, select=5, output=1)


#FORECASTE SEASONAL COMPONENT  
#Holt Winter’s Exponential Smoothing forecast for seasonal component 
train, test, train_size = interval_test_train_split(wvtrans, 96)
#IMPROVE!!!
yhat = exp_smoothing_forecast(wvtrans[:train_size-96*4], ['mul', False, None, 0, False, False], k=96)
#Evaluate the prediction
evaluate_prediction(wvtrans[train_size-96*4:train_size-96*3], yhat)
yhat = pd.Series(yhat)
fin_seasonal_comp = wvtrans[:train_size-96*4].append(yhat, ignore_index=True)



#Deseasonalize Day-ahead Forecasting Error
#Choose which seasonal form is assumed 
#Additive or multiplicative Seasonality 

#Additive Model 
wvtrans.index = train_main_series.index
add_deseason = train_main_series['Forecasting Error'] - wvtrans

#Multiplicative Model 
wvtrans.index = train_main_series.index
mulp_deseason = np.log(train_main_series['Forecasting Error'])- np.log(wvtrans)


#Forecast deseasonalized residual model with ARIMA in **.py


#Add seasonal component back to the residuals 
#Merge residual model with its prediction
x = deseason[:train_size-96*4]
des_full = x.append(predictions,ignore_index=True)


# Add deseasonalized series to transformed 

des_full.index = fin_seasonal_comp.index
back_transform = fin_seasonal_comp+des_full
back_transform.index = train_Dat_Ser[:train_size-96*3].index
evaluate_prediction( train_Dat_Ser['Forecasting Error']['2018-12-09 00:00:00':'2018-12-12 00:00:00'],back_transform['2018-12-09 00:00:00':'2018-12-12 00:00:00'])


plt.plot(wvtrans)
plt.show


