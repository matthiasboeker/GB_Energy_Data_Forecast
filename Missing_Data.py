#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:15:49 2019

@author: matthiasboeker
Deal with Missing Data"""

#MISSING DATA HAS TO BE DEALT WITH PROPER!!
#MUST BE ADJUSTED SCIENTIFICALLY!!


#finding na-values in datasets

load_nans_2016 = dat_series_2016[np.isnan(dat_series_2016.iloc[:,2])]
load_nans_2017 = dat_series_2017[np.isnan(dat_series_2017.iloc[:,2])]
load_nans_2018 = dat_series_2018[np.isnan(dat_series_2018.iloc[:,2])]
load_nans_2019 = dat_series_2019[np.isnan(dat_series_2019.iloc[:,2])]
load_nans_full = full_dat_series[np.isnan(full_dat_series.iloc[:,2])]

day_ahead_nans_2016 = dat_series_2016[np.isnan(dat_series_2016.iloc[:,1])]
day_ahead_nans_2017 = dat_series_2017[np.isnan(dat_series_2017.iloc[:,1])]
day_ahead_nans_2018 = dat_series_2018[np.isnan(dat_series_2018.iloc[:,1])]
day_ahead_nans_2019 = dat_series_2019[np.isnan(dat_series_2019.iloc[:,1])]
day_ahead_nans_full = full_dat_series[np.isnan(full_dat_series.iloc[:,1])]

#Approach: Using Total_Load as Replacement!

n_full_dat_series = pd.DataFrame(full_dat_series.values)
n_full_dat_series.columns = col_names[1:]
n_full_dat_series['Day-ahead Total Load Forecast'] = np.where(np.isnan(n_full_dat_series['Day-ahead Total Load Forecast']),n_full_dat_series.iloc[:,2],n_full_dat_series.iloc[:,1])
left_nan = n_full_dat_series[np.isnan(n_full_dat_series['Day-ahead Total Load Forecast'])]

#Transforming the series into a matrix icluding daily series'
cc = np.array(n_full_dat_series.iloc[0:48,1].values)
for i in range(48,len(n_full_dat_series)-48,48):
    new_cc = n_full_dat_series.iloc[i:i+48,1]
    cc = np.vstack([cc,new_cc])
cc = cc.T

#fill na's by propagate last valid observation forward to next valid 
cc = pd.DataFrame(cc)
cc = cc.fillna(method='ffill',axis=1)

np.sqrt(dat_series_2017['Total Load']).hist(bins=100)
