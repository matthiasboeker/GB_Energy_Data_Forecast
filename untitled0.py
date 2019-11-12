#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:17:55 2019

@author: matthiasboeker
Explorative Analysis"""
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.statespace.tools import diff
"Examine TS for Stationarity 

print(' First half of 2016, Var:',np.var(dat_series_2016.iloc[0:int(len(dat_series_2016)/2),3]))
print(' Second half of 2016, Var:',np.var(dat_series_2016.iloc[int(len(dat_series_2016)/2):,3]))
print(' Difference between, Var:',np.var(dat_series_2016.iloc[0:int(len(dat_series_2016)/2),3])-np.var(dat_series_2016.iloc[int(len(dat_series_2016)/2):,3]))

print(' First half of 2017, Var:',np.var(dat_series_2017.iloc[0:int(len(dat_series_2017)/2),3]))
print(' Second half of 2017, Var:',np.var(dat_series_2017.iloc[int(len(dat_series_2017)/2):,3]))
print(' Difference between, Var:',np.var(dat_series_2017.iloc[0:int(len(dat_series_2017)/2),3])-np.var(dat_series_2017.iloc[int(len(dat_series_2017)/2):,3]))


print(' First half of 2018, Var:',np.var(dat_series_2018.iloc[0:int(len(dat_series_2018)/2),3]))
print(' Second half of 2018, Var:',np.var(dat_series_2018.iloc[int(len(dat_series_2018)/2):,3]))
print(' Difference between, Var:',np.var(dat_series_2018.iloc[0:int(len(dat_series_2018)/2),3])-np.var(dat_series_2018.iloc[int(len(dat_series_2018)/2):,3]))


print(' First half of 2019, Var:',np.var(dat_series_2019.iloc[0:int(len(dat_series_2019)/2),3]))
print(' Second half of 2019, Var:',np.nanvar(dat_series_2019.iloc[int(len(dat_series_2019)/2):,3]))
print(' Difference between, Var:',np.var(dat_series_2019.iloc[0:int(len(dat_series_2019)/2),3])-np.var(dat_series_2019.iloc[int(len(dat_series_2019)/2):,3]))

'Testing for stationarity 
kpsstest_2016 = kpss(diff(dat_series_2016.iloc[:,3].dropna()), regression='c')
kpsstest_2017 = kpss(dat_series_2017.iloc[:,3].dropna(), regression='ct')
kpsstest_2018 = kpss(dat_series_2018.iloc[:,3].dropna(), regression='ct')
kpsstest_2019 = kpss(dat_series_2019.iloc[:,3].dropna(), regression='ct')

adf_test_2016 = adfuller(dat_series_2016.iloc[:,3].dropna())
adf_test_2017 = adfuller(dat_series_2017.iloc[:,3].dropna())
adf_test_2018 = adfuller(dat_series_2018.iloc[:,3].dropna())
adf_test_2019 = adfuller(dat_series_2019.iloc[:,3].dropna())


plot_acf(diff(dat_series_2016.iloc[:,3].dropna(),k_diff=1), lags = 50)