#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 11:51:33 2019

@author: matthiasboeker
Data Preparation"""

from sklearn.preprocessing import MinMaxScaler



#Calculate Error between Total Load and Day-Ahead 

#Drop NaN Time shift and double hours
full_dat_series = full_dat_series.fillna(method='ffill')
full_dat_series = full_dat_series.drop([7274,16011,24749])
full_dat_series = full_dat_series.drop(['Date'],axis=1)
full_dat_series.index = pd.date_range(start= '2016-01-01 00:00:00', end='2019-06-14 23:00:00', freq = 'h')
#Delete the 29. February
full_dat_series = full_dat_series.loc[(full_dat_series.index < '2016-02-29 00:00:00') | (full_dat_series.index > '2016-02-29 23:00:00')]

full_dat_series = full_dat_series['2016-01-01 00:00:00':'2019-06-13 00:00:00']
full_dat_series['Total Load'] = full_dat_series['Total Load'].astype(float)

#Differencing Time Series 
full_dat_series['Forecasting Error'] = full_dat_series['Total Load']-full_dat_series['Day-ahead Total Load Forecast']

#Outliner detection 
threshold1 = np.std(full_dat_series['Forecasting Error'])*4
threshold2 = -1*threshold1
full_dat_series['Forecasting Error'] = full_dat_series['Forecasting Error'].apply(lambda x: x if (x >threshold2)and(x <= threshold1) else np.nan) 
full_dat_series['Forecasting Error'] = full_dat_series['Forecasting Error'].fillna(method='ffill')

#Normalisiere Daten 
values = full_dat_series['Forecasting Error']
values = values.reshape((len(values), 1))
# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print the first 5 rows
normalized = scaler.transform(values)
full_dat_series['Forecasting Error'] = normalized


#Time Series for each Year 
dat_series_16 = full_dat_series['2016-01-01 00:00:00':'2017-01-01 00:00:00']
dat_series_17 = full_dat_series['2017-01-01 00:00:00':'2018-01-01 00:00:00']
dat_series_18 = full_dat_series['2018-01-01 00:00:00':'2019-01-01 00:00:00']
dat_series_19 = full_dat_series['2019-01-01 00:00:00':]






