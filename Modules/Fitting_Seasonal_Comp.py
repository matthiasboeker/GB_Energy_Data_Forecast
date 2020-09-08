#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:33:55 2020

@author: matthiasboeker
Modelling the seasonal component"""
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima_model import ARIMA


#Try to fit the model with Holt Winter's Exponential Smoothing Forecast
#Holt Winter’s Exponential Smoothing forecast for seasonal component 
train, test, train_size = interval_test_train_split(wvtrans, 96*4)
yhat = exp_smoothing_forecast(wvtrans[:train_size-96*4], ['mul', False, None, 0, False, False], k=96)
#Evaluate the prediction
evaluate_prediction(wvtrans[train_size-96*4:train_size-96*3], yhat)

#Deterministic modelling of the seasonal component 

#Wavelet Transform and Backtransform and extract the seasonal component 
wvtrans_16 = wavelet_signal_select(dat_series_16['Forecasting Error'], wavelet='db7', levels= 7, plot=False, select=7, output=1)
wvtrans_17 = wavelet_signal_select(dat_series_17['Forecasting Error'], wavelet='db7', levels= 7, plot=False, select=7, output=1)
wvtrans_18 = wavelet_signal_select(dat_series_18['Forecasting Error'], wavelet='db7', levels= 7, plot=False, select=7, output=1)
wvtrans_mean = pd.DataFrame(np.mean([wvtrans_16.values,wvtrans_17.values,wvtrans_18.values],axis=0))





#Generate a mean without each year respectively 
mean_w_16 = pd.DataFrame(np.mean([wvtrans_17.values,wvtrans_18.values],axis=0))
mean_w_17 = pd.DataFrame(np.mean([wvtrans_16.values,wvtrans_18.values],axis=0))
mean_w_18 = pd.DataFrame(np.mean([wvtrans_16.values,wvtrans_17.values],axis=0))


#Plot the three seasonal components and the mean 
seasonal_comps = plt.figure(figsize=(10,5))
chart_seas_comp = seasonal_comps.add_subplot(211)
chart_seas_comp.plot(wvtrans_16)
chart_seas_comp.plot(wvtrans_17)
chart_seas_comp.plot(wvtrans_18)
chart_seas_comp.plot(wvtrans_mean)
plt.ylabel('Seasonal Components')
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/Extracted_Seasonal_component.png')
plt.show()

seasonal_comps = plt.figure(figsize=(10,5))
chart_seas_comp1 = seasonal_comps.add_subplot(221)
chart_seas_comp2 = seasonal_comps.add_subplot(222)
chart_seas_comp3 = seasonal_comps.add_subplot(223)
chart_seas_comp4 = seasonal_comps.add_subplot(224)
chart_seas_comp1.plot(wvtrans_16)
plt.ylabel('Seasonal Components 2916')
chart_seas_comp2.plot(wvtrans_17, color='darkcyan')
plt.ylabel('Seasonal Components 2017')
chart_seas_comp3.plot(wvtrans_18,color='seagreen')
plt.ylabel('Seasonal Components 2018')
chart_seas_comp4.plot(wvtrans_mean,color='maroon')
plt.ylabel('Seasonal Components Mean')
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/Extracted_Seasonal_component.png')
plt.show()

#Generate a mean without each year respectively 
mean_w_16 = pd.DataFrame(np.mean([wvtrans_17.values,wvtrans_18.values],axis=0))
mean_w_17 = pd.DataFrame(np.mean([wvtrans_16.values,wvtrans_18.values],axis=0))
mean_w_18 = pd.DataFrame(np.mean([wvtrans_16.values,wvtrans_17.values],axis=0))

seasonal_comps = plt.figure(figsize=(10,5))
chart_seas_mean1 = seasonal_comps.add_subplot(221)
chart_seas_mean2 = seasonal_comps.add_subplot(222)
chart_seas_mean3 = seasonal_comps.add_subplot(223)
chart_seas_comp4 = seasonal_comps.add_subplot(224)
chart_seas_mean1.plot(mean_w_16)
plt.ylabel('Seasonal  Mean without 2016')
chart_seas_mean2.plot(mean_w_17, color='darkcyan')
plt.ylabel('Seasonal Mean without 2017')
chart_seas_mean3.plot(mean_w_18,color='seagreen')
plt.ylabel('Seasonal Mean without 2018')
chart_seas_comp4.plot(wvtrans_mean,color='maroon')
plt.ylabel('Seasonal Components Mean')
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/Forecasting_Err_16_comp_year.png')
plt.show()


