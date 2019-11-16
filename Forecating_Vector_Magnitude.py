#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:01:12 2019

@author: matthiasboeker
Predicting the magnitude of the data vector"""

from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf


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
dif_mag_ts = difference(mag_ts,7)

#KPSS and ADFULLER TEST

adfuller_res = adfuller(dif_mag_ts)
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(dif_mag_ts)
'KPSS Test rejects H0 -> TS is non stationary'

#Plot Magnitude of TS
plt.plot(dif_mag_ts[1100:])
plt.ylabel('Magnitude')
plt.show()

#PLot ACF PACF
plot_acf(mag_ts, lags=500)
plot_pacf(mag_ts, lags=500)

#PLot Diff ACF PACF
plot_acf(dif_mag_ts, lags=50)
plot_pacf(dif_mag_ts, lags=50)

'Seasonal adjusted plots indicate a SARMA(P=0, D=1,Q=1) Model
import statsmodels.api as sm

morder=(0,1,1)
sorder=(1,1,0,9)
model = sm.tsa.statespace.SARIMAX(mag_ts, order=morder,seasonal_order=sorder)
model_fit = model.fit(disp=0)
print(model_fit.summary())
yhat = model_fit.forecast(steps=24)

plt.plot(mag_ts[1200:])
plt.plot(yhat)
plt.ylabel('Magnitude')
plt.show()

