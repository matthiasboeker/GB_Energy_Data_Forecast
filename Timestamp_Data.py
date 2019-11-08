#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:37:27 2019

@author: matthiasboeker
"""

import pandas as pd
import numpy as np
import datetime 


col_names = ['Time','Date', 'Day-ahead Total Load Forecast', 'Total Load']
full_dat_series = pd.read_csv('GB_Loading_Data_full_series.csv', sep =';',skiprows=[0], names=col_names )
2016_dat_series = pd.read_csv('GB_Loading_Data_2016.csv', sep =';',skiprows=[0], names=col_names  )
2017_dat_series = pd.read_csv('GB_Loading_Data_2017.csv', sep =';',skiprows=[0], names=col_names )
2018_dat_series = pd.read_csv('GB_Loading_Data_2018.csv', sep =';',skiprows=[0], names=col_names )
2019_dat_series = pd.read_csv('GB_Loading_Data_2019.csv', sep =';',skiprows=[0], names=col_names )

full_dat_series.iloc[:,2:3].astype('float')
full_dat_series.iloc[:,1] = full_dat_series.iloc[:,1].str.cat(full_dat_series.iloc[:,0].str[8:], sep =" ")
full_dat_series.iloc[:,1] = pd.to_datetime(full_dat_series.iloc[:,1])
full_dat_series = full_dat_series.iloc[:,1:]

2016_dat_series.iloc[:,2:3].astype('float')
2016_dat_series.iloc[:,1] = full_dat_series.iloc[:,1].str.cat(full_dat_series.iloc[:,0].str[8:], sep =" ")
2016_dat_series.iloc[:,1] = pd.to_datetime(full_dat_series.iloc[:,1])
2016_dat_series = full_dat_series.iloc[:,1:]

2017_dat_series.iloc[:,2:3].astype('float')
2017_dat_series.iloc[:,1] = full_dat_series.iloc[:,1].str.cat(full_dat_series.iloc[:,0].str[8:], sep =" ")
2017_dat_series.iloc[:,1] = pd.to_datetime(full_dat_series.iloc[:,1])
2017_dat_series = full_dat_series.iloc[:,1:]

2018_dat_series.iloc[:,2:3].astype('float')
2018_dat_series.iloc[:,1] = full_dat_series.iloc[:,1].str.cat(full_dat_series.iloc[:,0].str[8:], sep =" ")
2018_dat_series.iloc[:,1] = pd.to_datetime(full_dat_series.iloc[:,1])
2018_dat_series = full_dat_series.iloc[:,1:]

2019_dat_series.iloc[:,2:3].astype('float')
2019_dat_series.iloc[:,1] = full_dat_series.iloc[:,1].str.cat(full_dat_series.iloc[:,0].str[8:], sep =" ")
2019_dat_series.iloc[:,1] = pd.to_datetime(full_dat_series.iloc[:,1])
2019_dat_series = full_dat_series.iloc[:,1:]