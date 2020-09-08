#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:06:55 2019

@author: matthiasboeker
Fit SARIMA Model for each Year""""
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller, kpss
import statsmodels.api as sm
from matplotlib import pyplot as plt 


#Check plotted ts16

fig_16_c = plt.figure(figsize=(10,5))
chart_16_c = fig_16_c.add_subplot(111)
chart_16_c.plot(dat_series_16['Forecasting Error'])
plt.ylabel('Forecasting Error')
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/Forecasting_Err_16_comp_year.png')
plt.show()

#Check if variance is stable 
print('First part variance:',np.var(dat_series_16['Forecasting Error'][:int(len(dat_series_16)/3)]))
print('Second part variance:',np.var(dat_series_16['Forecasting Error'][int(len(dat_series_16)/3):int(len(dat_series_16)*(2/3))]))
print('Third part variance:',np.var(dat_series_16['Forecasting Error'][int(len(dat_series_16)*(2/3)):]))
#No bigger differences -> assume it is stable 


#KPSS and ADFULLER TEST

adfuller_res = adfuller(dat_series_16['Forecasting Error'])
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(dat_series_16['Forecasting Error'])
'KPSS Test rejects H0 -> TS is non stationary'

#Plot ACF and PACF
plot_acf(dat_series_16['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(dat_series_16['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')

#Differentiating about the 24th lag 
diff = dat_series_16.diff(24)
diff = diff[25:]

#Plot diffed ACF and PACF
plot_acf(diff['Forecasting Error'], lags=20)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/diff_acf_16.png')
plot_pacf(diff['Forecasting Error'], lags=20)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/diff_pacf_16.png')


#First guess (1,0,0)x(0,1,1,24)
morder=(1,0,0)
sorder=(0,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_16['Forecasting Error'], order=morder,seasonal_order=sorder)
model1_16_fit = model.fit(disp=0)
print(model1_16_fit.summary())

model1_16_fit.plot_diagnostics()
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5//diagnostics1.png')

pred1 = model1_16_fit.get_prediction(start=len(dat_series_16)-96*4, end=len(dat_series_16)-96*3)
evaluate_prediction2(dat_series_16['Forecasting Error'][len(dat_series_16)-96*4:len(dat_series_16)-96*3],pred1)
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/prediction1.png')



#Second guess (2,0,0)x(0,1,1,24)
morder=(2,0,0)
sorder=(0,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_16, order=morder,seasonal_order=sorder)
model2_16_fit = model.fit(disp=0)
print(model2_16_fit.summary())


model2_16_fit.plot_predict()
model2_16_fit.plot_diagnostics()
predictions2= model2_16_fit.predict(start=train_16,end=train_16+96-1)
evaluate_prediction(dat_series_16['Forecasting Error'][len(dat_series_16)-96*4:len(dat_series_16)-96*3], predictions2)

#Third guess (1,0,1)x(0,1,1,24)
morder=(1,0,1)
sorder=(0,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_16, order=morder,seasonal_order=sorder)
model3_16_fit = model.fit(disp=0)
print(model3_16_fit.summary())
model3_16_fit.prediction()

model3_16_fit.plot_diagnostics()
predictions3= model3_16_fit.predict(start=train_16,end=train_16+96-1)
evaluate_prediction(dat_series_16['Forecasting Error'][len(dat_series_16)-96*4:len(dat_series_16)-96*3], predictions3)

#Fourth guess (1,0,0)x(1,1,1,24)
morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_16['Forecasting Error'], order=morder,seasonal_order=sorder)
model4_16_fit = model.fit(disp=0)
print(model4_16_fit.summary())

model4_16_fit.plot_diagnostics()
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/diagnostics_end_16.png')
predictions4= model4_16_fit.get_prediction(start=train_size_16,end=train_size_16+96-1)
evaluate_prediction2(dat_series_16['Forecasting Error'][len(dat_series_16)-96*4:len(dat_series_16)-96*3], predictions4)



#*******************************************************************************************************************************

#plotting ts17
fig_17_c = plt.figure(figsize=(10,5))
chart_17_c = fig_17_c.add_subplot(111)
chart_17_c.plot(dat_series_17['Forecasting Error'])
plt.ylabel('Forecasting Error')
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/Forecasting_Err_16_comp_year.png')
plt.show()


#Check if variance is stable 
print('First part variance:',np.var(dat_series_17['Forecasting Error'][:int(len(dat_series_17)/3)]))
print('Second part variance:',np.var(dat_series_17['Forecasting Error'][int(len(dat_series_17)/3):int(len(dat_series_17)*(2/3))]))
print('Third part variance:',np.var(dat_series_17['Forecasting Error'][int(len(dat_series_17)*(2/3)):]))
#No bigger differences -> assume it is stable 

#KPSS and ADFULLER TEST

adfuller_res = adfuller(dat_series_17['Forecasting Error'])
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(dat_series_17['Forecasting Error'])
'KPSS Test rejects H0 -> TS is non stationary'

#Plot ACF and PACF
plot_acf(dat_series_17['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(dat_series_17['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')

#Differentiating about the 24th lag 
diff = dat_series_17.diff(24)
diff = diff[25:]

#Plot diffed ACF and PACF
plot_acf(diff['Forecasting Error'], lags=500)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/diff_acf_16.png')
plot_pacf(diff['Forecasting Error'], lags=120)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/diff_pacf_16.png')


#Applying best choice model to 2017 data 

#First guess (1,0,0)x(1,1,1,24)
morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_17['Forecasting Error'], order=morder,seasonal_order=sorder)
model1_17_fit = model.fit(disp=0)
print(model1_17_fit.summary())

model1_17_fit.plot_diagnostics()
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/diagnostics17.png')
predictions5= model1_17_fit.get_prediction(start=train_17,end=train_17+96-1)
evaluate_prediction2(dat_series_17['Forecasting Error'][len(dat_series_17)-96*4:len(dat_series_17)-96*3], predictions5)

#Second guess, most simple one (1,0,0)x(0,1,1,24)
morder=(1,0,0)
sorder=(0,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_17, order=morder,seasonal_order=sorder)
model2_17_fit = model.fit(disp=0)

print(model2_17_fit.summary())

model2_17_fit.plot_diagnostics()
predictions6= model2_17_fit.get_prediction(start=train_17,end=train_17+96-1)
evaluate_prediction2(dat_series_17['Forecasting Error'][len(dat_series_17)-96*4:len(dat_series_17)-96*3], predictions6)

#Trying to cover the apparent randomness with a seasonal withe noise 
morder=(0,1,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_17, order=morder,seasonal_order=sorder)
model3_17_fit = model.fit(disp=0)
print(model3_17_fit.summary())

model3_17_fit.plot_diagnostics()
predictions7= model3_17_fit.get_prediction(start=train_17,end=end=train_17+96-1)
evaluate_prediction2(dat_series_17['Forecasting Error'][len(dat_series_17)-96*4:len(dat_series_17)-96*3], predictions7)
#-> no improvement 


#*******************************************************************************************************************************

#plotting ts17
fig_18_c = plt.figure(figsize=(10,5))
chart_18_c = fig_18_c.add_subplot(111)
chart_18_c.plot(dat_series_18['Forecasting Error'])
plt.ylabel('Forecasting Error')
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5//Forecasting_Err_18_comp_year.png')
plt.show()


#Check if variance is stable 
print('First part variance:',np.var(dat_series_18['Forecasting Error'][:int(len(dat_series_17)/3)]))
print('Second part variance:',np.var(dat_series_18['Forecasting Error'][int(len(dat_series_17)/3):int(len(dat_series_17)*(2/3))]))
print('Third part variance:',np.var(dat_series_18['Forecasting Error'][int(len(dat_series_17)*(2/3)):]))
#No bigger differences -> assume it is stable 

#KPSS and ADFULLER TEST

adfuller_res = adfuller(dat_series_18['Forecasting Error'])
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(dat_series_18['Forecasting Error'])
'KPSS Test rejects H0 -> TS is non stationary'

#Plot ACF and PACF
plot_acf(dat_series_17['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/acf_16.png')
plot_pacf(dat_series_17['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/pacf_16.png')

#Differentiating about the 24th lag 
diff = dat_series_18.diff(24)
diff = diff[25:]

#Plot diffed ACF and PACF
plot_acf(diff['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/diff_acf_16.png')
plot_pacf(diff['Forecasting Error'], lags=50)
#plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Chapter Notes /Chapter 5/diff_pacf_16.png')



#Applying best choice model to from diagnostics

#First guess (1,0,0)x(1,1,1,24)
morder=(1,0,0)
sorder=(0,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_18, order=morder,seasonal_order=sorder)
model1_18_fit = model.fit(disp=0)
print(model1_18_fit.summary())

model1_18_fit.plot_diagnostics()
predictions8= model1_18_fit.get_prediction(start=train_18,end=train_18+96-1)
evaluate_prediction2(dat_series_18['Forecasting Error'][len(dat_series_18)-96*4:len(dat_series_18)-96*3], predictions8)


#Second guess, seasonal white noise
morder=(0,1,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_18, order=morder,seasonal_order=sorder)
model2_18_fit = model.fit(disp=0)
print(model2_18_fit.summary())

model2_18_fit.plot_diagnostics()
predictions10= model2_18_fit.get_prediction(start=train_18,end=end=train_18+96-1)
evaluate_prediction2(dat_series_18['Forecasting Error'][len(dat_series_18)-96*4:len(dat_series_18)-96*3], predictions10)


#Third guess, best choice from 2017
morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(train_18['Forecasting Error'], order=morder,seasonal_order=sorder)
model3_18_fit = model.fit(disp=0)
print(model3_18_fit.summary())

model3_18_fit.plot_diagnostics()
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5//diagnostics_18.png')
predictions11= model3_18_fit.get_prediction(start=train_18,end=end=train_18+96-1)
evaluate_prediction2(dat_series_18['Forecasting Error'][len(dat_series_18)-96*4:len(dat_series_18)-96*3], predictions11)



