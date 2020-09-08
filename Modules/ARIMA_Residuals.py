#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:37:12 2019

@author: matthiasboeker
Fit a ARIMA Model to the Residuals"""
import pandas as pd
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.stattools import adfuller,kpss
import statsmodels.api as sm


#Choose deseasonalized model 
#Additive
deseason_16 = add_deseason_16
deseason_17 = add_deseason_17
deseason_18 = add_deseason_18

EST_16 = pd.DataFrame(dat_series_16['Forecasting Error'][:len(train_16)])
EST_16['Error']= deseason_16[:len(train_16)]
EST_16['Seasonal Component'] = mean_w_16[:len(train_16)]

#Plotting Seasonal Component, Error and Raw Data
EST_16['Forecasting Error'].plot(legend=True)
EST_16['Seasonal Component'].plot( legend=True)
EST_16['Error'].plot(legend= True )
plt.show()

#********************************************************************************************
#Resiudal Model for 2016

#KPSS and ADFULLER TEST
adfuller_res = adfuller(deseason_16)
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(deseason_16)
'KPSS Test rejects H0 -> TS is non stationary'

deseas_diff = deseas_diff.diff(24)
deseas_diff = deseas_diff[25:]

plot_acf(deseas_diff, lags=100)
plot_pacf(deseas_diff, lags=100)


#Model ARIMA
morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(deseason_16[:len(deseason_16)-96*4], order=morder,seasonal_order=sorder)
model1_res16_fit = model.fit(disp=0)

print(model1_res16_fit.summary())
model1_res16_fit.plot_diagnostics()
predictions_res_1= model1_res16_fit.get_prediction(start=len(train_16),end=len(train_16)+96-1)
evaluate_prediction(deseason_16[len(train_16):len(train_16)+96], predictions_res_1.predicted_mean)

#Model Arima with endogenous variable 

#Allign indices
wvtrans_mean.index = dat_series_16['Forecasting Error'].index

morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(dat_series_16['Forecasting Error'][:len(dat_series_16)-96*4], exog=wvtrans_mean[:len(dat_series_16)-96*4], order=morder,seasonal_order=sorder)
exog_16_model = model.fit(disp=0)
print(exog_16_model.summary())

#Ljung Box Test 
line = np.repeat(0.05, len(lj_test_statistic16[0][1]))
lj_test_statistic16 = exog_16_model.test_serial_correlation('ljungbox')
plt.plot(lj_test_statistic16[0][1])
plt.ylabel('p-Values')
plt.xlabel('Lags')
plt.plot(line,linestyle='--')
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/ljung_box_exog_16.png')

#Diagnostics
exog_16_model.plot_diagnostics()
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/diagnostics_exog_16.png')

predictions_exog1= exog_16_model.get_prediction(start=len(train_16),end=len(train_16)+96-1, exog=wvtrans_mean[len(dat_series_16)-96*4:len(dat_series_16)-96*3-1])
a = dat_series_16['Forecasting Error'][len(dat_series_16)-96*4:len(dat_series_16)-96*3]
a.index = predictions_exog1.predicted_mean.index
evaluate_prediction2(a, predictions_exog1)
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/predictions_exog_16.png')





#********************************************************************************************
#Resiudal Model for 2017
#KPSS and ADFULLER TEST
adfuller_res = adfuller(deseason_17)
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(deseason_17)
'KPSS Test rejects H0 -> TS is non stationary'

deseas_diff_17 = deseason_17.diff(24)
deseas_diff_17 = deseas_diff[25:]

plot_acf(deseas_diff_17, lags=50)
plot_pacf(deseas_diff_17, lags=50)


#Model ARIMA
morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(deseason_17[:len(deseason_17)-96*4], order=morder,seasonal_order=sorder)
model1_res17_fit = model.fit(disp=0)

print(model1_res17_fit.summary())
model1_res17_fit.plot_diagnostics()
predictions_res_2= model1_res17_fit.get_prediction(start=len(train_17),end=len(train_17)+96-1)
evaluate_prediction2(deseason_17[len(train_17):len(train_17)+96], predictions_res_2)


#Model 2017 Arima with exogenous variable 

#Allign indices
wvtrans_mean.index = dat_series_17['Forecasting Error'].index

morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(dat_series_17['Forecasting Error'][:len(dat_series_17)-96*4], exog=wvtrans_mean[:len(dat_series_17)-96*4], order=morder,seasonal_order=sorder)
exog_17_model = model.fit(disp=0)
print(exog_17_model.summary())
exog_17_model.plot_diagnostics()
predictions_exog2= exog_17_model.get_prediction(start=len(train_17),end=len(train_17)+96-1, exog=wvtrans_mean[len(dat_series_17)-96*4:len(dat_series_17)-96*3-1])
a = dat_series_17['Forecasting Error'][len(dat_series_17)-96*4:len(dat_series_17)-96*3]
a.index = predictions_exog2.predicted_mean.index
evaluate_prediction2(a, predictions_exog2)
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/predictions_exog_17.png')




#********************************************************************************************
#Resiudal Model for 2018
#Model ARIMA
morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(deseason_18[:len(deseason_18)-96*4], order=morder,seasonal_order=sorder)
model1_res18_fit = model.fit(disp=0)

print(model1_res18_fit.summary())
model1_res18_fit.plot_diagnostics()
predictions_res_3= model1_res18_fit.get_prediction(start=len(train_18),end=len(train_18)+96-1)
evaluate_prediction2(deseason_18[len(train_18):len(train_18)+96], predictions_res_3)





#Allign indices
wvtrans_mean.index = dat_series_18['Forecasting Error'].index

morder=(1,0,0)
sorder=(1,1,1,24)
model = sm.tsa.statespace.SARIMAX(dat_series_18['Forecasting Error'][:len(dat_series_18)-96*4], exog=wvtrans_mean[:len(dat_series_18)-96*4], order=morder,seasonal_order=sorder)
exog_18_model = model.fit(disp=0)
print(exog_18_model.summary())
exog_18_model.plot_diagnostics()
predictions_exog3= exog_18_model.get_prediction(start=len(train_18),end=len(train_18)+96-1, exog=wvtrans_mean[len(dat_series_18)-96*4:len(dat_series_18)-96*3-1])
a = dat_series_18['Forecasting Error'][len(dat_series_18)-96*4:len(dat_series_18)-96*3]
a.index = predictions_exog3.predicted_mean.index
evaluate_prediction2(a, predictions_exog3)
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/predictions_exog_18.png')



