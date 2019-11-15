#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:12 2019

@author: matthiasboeker
Predicting the magnitude of the data vector"""

from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima

def magnitude(dataset):
    mag = np.zeros(dataset.shape[1])
    for i in range(0, dataset.shape[1]):
        mag[i] = np.linalg.norm(dataset.iloc[:,i])
    return pd.DataFrame(mag)


def difference(dataset, interval=1):
    ar = np.zeros(dataset.shape[0]-1)
    for i in range(interval, dataset.shape[0]):
        ar[i-interval] = dataset.iloc[i] - dataset.iloc[i - interval]
    return ar


mag_ts = magnitude(cc)
dif_mag_ts = difference(mag_ts)

#KPSS and ADFULLER TEST
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

adfuller_res = adfuller(mag_ts)
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(mag_ts)
'KPSS Test rejects H0 -> TS is non stationary'



stepwise_model = auto_arima(dif_mag_ts, start_p=1, start_q=1,
                           max_p=5, max_q=5, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)
print(stepwise_model.aic())


train = dif_mag_ts[0:int(len(dif_mag_ts)*0.8)]
test = dif_mag_ts[0:int(len(dif_mag_ts)-len(dif_mag_ts)*0.8)]
test = pd.DataFrame(test)

stepwise_model.fit(train)
future_forecast = stepwise_model.predict(n_periods=50)

future_forecast = pd.DataFrame(future_forecast)
plt.plot(pd.concat([test[0:50],future_forecast],axis=1))
plt.ylabel('Cosine Similarity')
plt.show()




