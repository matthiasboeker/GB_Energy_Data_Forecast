#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 01:06:55 2019

@author: matthiasboeker
"""
"Analyzing Timeseries"
import pandas as pd
import numpy as np


#Safe TS as DF
csts = pd.DataFrame(cos_sim)
csts.hist(bins=50)

#Outliner detection 
plt.plot(csts)
plt.ylabel('Cosine Similarity')
plt.show()

outliner = np.where(csts<0.96)[0]

#For simplicity: Replace outliner with mean 
csts.iloc[outliner] = [np.mean(csts),np.mean(csts),np.mean(csts)]

#Check plotted ts
plt.plot(csts)
plt.ylabel('Cosine Similarity')
plt.show()


#Smoothing the Data 
sm_csts = csts.rolling(window=10).mean()

#Plot smoothed TS
plt.plot(sm_csts)
plt.ylabel('Smoothed Cosine Similarity')
plt.show()

#Testing for Stationarity 
sm_csts.hist()

#Examine variance of the first and second half
split = int(len(sm_csts) / 2)
sm_csts1, sm_csts2 = sm_csts[0:split], sm_csts[split:]
mean1, mean2 = sm_csts1.mean(), sm_csts2.mean()
var1, var2 = sm_csts1.var(), sm_csts2.var()
print('Variance 1:', var1, 'Variance 2:', var2)

#KPSS and ADFULLER TEST
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

adfuller_res = adfuller(csts[0])
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(csts[0])
'KPSS Test rejects H0 -> TS is non stationary'

#Try to differenciate TS
dif_csts = difference(csts,1)
adfuller_res = adfuller(dif_csts)
'AdFuller Test rejects H0 -> TS is stationary'
kpss_res = kpss(dif_csts)
'KPSS Test rejects H0 -> TS is non stationary'







