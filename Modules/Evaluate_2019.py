#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 22:47:36 2020

@author: matthiasboeker
Evaluating SARIMA model on 2019 respectively"""
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

#Best choice model (1,0,0)x(1,1,1)
#Fit model to 2019 March on 

#Getting start_params from 2018 model 
sparams = model3_18_fit.start_params

morder=(1,1,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(dat_series_19['Forecasting Error']['2019-01-01 00:00:00':],order=morder,seasonal_order=sorder)
model1_19_fit = model.fit(disp=0)
print(model1_19_fit.summary())

model1_19_fit.plot_diagnostics()

#Plotting the residuals of 16 17 18 19
residuals_16 = model4_16_fit.resid
residuals_17 = model1_16_fit.resid
residuals_18 = model3_16_fit.resid
residuals_19 = model1_19_fit.resid

#plotting residuals of 2019
fig_19_res = plt.figure(figsize=(10,5))
chart_19_res = fig_19_res.add_subplot(111)
chart_19_res.plot(residuals_19['2019-01-01 00:00:00':'2019-02-01 00:00:00'])
plt.ylabel('Model Residuals')
plt.show()
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/Forecasting_Err_16_comp_year.png')

#Plot ACF and PACF of Model Residuals for each year 
#2016
plot_acf(residuals_16, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(residuals_16, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')
#2017
plot_acf(residuals_17, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(residuals_17, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')
#2018
plot_acf(residuals_18, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(residuals_18, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')
#2019
plot_acf(residuals_19, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(residuals_19, lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')

#For each year expect 2019 (maybe too little data) still a slight seasonality could be detected within the resiudals of the model


    