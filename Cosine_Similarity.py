#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:53:21 2019

@author: matthiasboeker
"""
#Create Cosine Similarity Matrix 
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

#Safe TS as DF
full_dat_series = full_dat_series.fillna(method='ffill')
ts = pd.DataFrame(full_dat_series['Total Load'][:30219],dtype='float64')
ts.hist(bins=50)

#Transforming the series into a matrix icluding daily series'
cc = np.array(ts.iloc[0:24].values)
for i in range(48,len(ts)-24,24):
    new_cc = ts.iloc[i:i+24]
    cc = np.hstack([cc,new_cc])

cc = pd.DataFrame(cc,dtype='float64')

#Calculating Cosine Similarity Time Series
cos_sim = np.zeros(cc.shape[1]-1)
for i in range(1, cc.shape[1]):
        cos_sim[i-1] = cosine_similarity(cc.iloc[:,i].values.reshape(1,-1),cc.iloc[:,i-1].values.reshape(1, -1))

#Forecasting Cosine Similarity

#Plot Cosine Similarity TS
plt.plot(cos_sim)
plt.ylabel('Cosine Similiarty')
plt.show()

#Outliner detection 
outliner = np.where(cos_sim<0.97)[0]

#For simplicity: Replace outliner with mean 
cos_sim[outliner] = np.repeat(np.mean(csts),4)

#Smoothing the Data 
cos_sim = pd.DataFrame(cos_sim)
sm_csts = cos_sim.rolling(window=10).mean()

#Plot smoothed TS
plt.plot(sm_csts)
plt.ylabel('Smoothed Cosine Similarity')
plt.show()


#KPSS and ADFULLER TEST

adfuller_res = adfuller(sm_csts)
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(sm_csts)
'KPSS Test rejects H0 -> TS is non stationary'


dif_cos_sim = difference(cos_sim,7)

#PLot ACF PACF
plot_acf(cos_sim, lags=50)
plot_pacf(cos_sim, lags=50)

#PLot Diff ACF PACF
plot_acf(dif_cos_sim, lags=50)
plot_pacf(dif_cos_sim, lags=50)

'Seasonal adjusted plots indicate a SARMA(P=0, D=1,Q=1) Model
import statsmodels.api as sm

morder=(7,1,0)
sorder=(0,1,1,7)
model = sm.tsa.statespace.SARIMAX(cos_sim[:1234], order=morder,seasonal_order=sorder)
model_fit = model.fit(disp=0)
print(model_fit.summary())
yhat = model_fit.forecast(steps=24)

plt.plot(cos_sim[1180:])
plt.plot(yhat)
plt.ylabel('Cosine Similarity')
plt.show()

