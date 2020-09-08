#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 16:50:46 2020

@author: matthiasboeker
Plotting Years"""

import matplotlib.pyplot as plt


#Plotting 2016 

plt.plot(dat_series_16['Forecasting Error'])
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_16.png')


#Plotting 2016 monthly 
plt.plot(dat_series_16['2016-01-01 00:00:00':'2016-02-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-02-01 00:00:00':'2016-03-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-03-01 00:00:00':'2016-04-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-04-01 00:00:00':'2016-05-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-05-01 00:00:00':'2016-06-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-06-01 00:00:00':'2016-07-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-07-01 00:00:00':'2016-08-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-08-01 00:00:00':'2016-09-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-09-01 00:00:00':'2016-10-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-10-01 00:00:00':'2016-11-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-11-01 00:00:00':'2016-12-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-12-01 00:00:00':'2017-01-01 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_16_monthly.png')

#Plotting 2016 weekly per month
plt.plot(dat_series_16['2016-01-01 00:00:00':'2016-01-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-02-01 00:00:00':'2016-02-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-03-01 00:00:00':'2016-03-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-04-01 00:00:00':'2016-04-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-05-01 00:00:00':'2016-05-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-06-01 00:00:00':'2016-06-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-07-01 00:00:00':'2016-07-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-08-01 00:00:00':'2016-08-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-09-01 00:00:00':'2016-09-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-10-01 00:00:00':'2016-10-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-11-01 00:00:00':'2016-11-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-12-01 00:00:00':'2016-12-07 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_16_weekly.png')


#Plotting 2016 daily per month Wednesday
plt.plot(dat_series_16['2016-01-13 00:00:00':'2016-01-14 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-02-10 00:00:00':'2016-02-11 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-03-09 00:00:00':'2016-03-10 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-04-06 00:00:00':'2016-04-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-05-04 00:00:00':'2016-05-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-06-08 00:00:00':'2016-06-09 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-07-06 00:00:00':'2016-07-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-08-03 00:00:00':'2016-08-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-09-07 00:00:00':'2016-09-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-10-05 00:00:00':'2016-10-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-11-09 00:00:00':'2016-11-10 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-12-07 00:00:00':'2016-12-08 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_16_daily_weekday.png')

#Plotting 2016 daily per month Sunday 
plt.plot(dat_series_16['2016-01-03 00:00:00':'2016-01-03 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-02-07 00:00:00':'2016-02-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-03-06 00:00:00':'2016-03-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-04-03 00:00:00':'2016-04-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-05-01 00:00:00':'2016-05-02 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-06-05 00:00:00':'2016-06-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-07-03 00:00:00':'2016-07-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-08-07 00:00:00':'2016-08-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-09-04 00:00:00':'2016-09-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-10-02 00:00:00':'2016-10-03 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-11-06 00:00:00':'2016-11-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_16['2016-12-04 00:00:00':'2016-12-05 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_16_weekend.png')




#Plotting 2017

plt.plot(dat_series_17['Forecasting Error'])
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_17.png')


#Plotting 2017 monthly 
plt.plot(dat_series_17['2017-01-01 00:00:00':'2017-02-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-02-01 00:00:00':'2017-03-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-03-01 00:00:00':'2017-04-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-04-01 00:00:00':'2017-05-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-05-01 00:00:00':'2017-06-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-06-01 00:00:00':'2017-07-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-07-01 00:00:00':'2017-08-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-08-01 00:00:00':'2017-09-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-09-01 00:00:00':'2017-10-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-10-01 00:00:00':'2017-11-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-11-01 00:00:00':'2017-12-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-12-01 00:00:00':'2018-01-01 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_17_monthly.png')

#Plotting 2017 weekly per month
plt.plot(dat_series_17['2017-01-01 00:00:00':'2017-01-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-02-01 00:00:00':'2017-02-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-03-01 00:00:00':'2017-03-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-04-01 00:00:00':'2017-04-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-05-01 00:00:00':'2017-05-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-06-01 00:00:00':'2017-06-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-07-01 00:00:00':'2017-07-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-08-01 00:00:00':'2017-08-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-09-01 00:00:00':'2017-09-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-10-01 00:00:00':'2017-10-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-11-01 00:00:00':'2017-11-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-12-01 00:00:00':'2018-12-07 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_17_weekly.png')


#Plotting 2017 daily per month Wednesday
plt.plot(dat_series_17['2017-01-04 00:00:00':'2017-01-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-02-08 00:00:00':'2017-02-09 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-03-08 00:00:00':'2017-03-09 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-04-05 00:00:00':'2017-04-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-05-10 00:00:00':'2017-05-11 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-06-07 00:00:00':'2017-06-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-07-05 00:00:00':'2017-07-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-08-09 00:00:00':'2017-08-10 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-09-06 00:00:00':'2017-09-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-10-04 00:00:00':'2017-10-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-11-08 00:00:00':'2017-11-09 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-12-06 00:00:00':'2018-12-07 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_17_daily_weekday.png')

#Plotting 2017 daily per month Sunday 
plt.plot(dat_series_17['2017-01-01 00:00:00':'2017-01-02 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-02-05 00:00:00':'2017-02-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-03-05 00:00:00':'2017-03-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-04-02 00:00:00':'2017-04-03 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-05-07 00:00:00':'2017-05-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-06-04 00:00:00':'2017-06-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-07-02 00:00:00':'2017-07-03 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-08-06 00:00:00':'2017-08-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-09-03 00:00:00':'2017-09-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-10-01 00:00:00':'2017-10-02 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-11-05 00:00:00':'2017-11-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_17['2017-12-03 00:00:00':'2018-12-04 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_17_weekend.png')

#Plotting 2018

plt.plot(dat_series_18['Forecasting Error'])
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_18.png')


#Plotting 2018 monthly 
plt.plot(dat_series_18['2018-01-01 00:00:00':'2018-02-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-02-01 00:00:00':'2018-03-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-03-01 00:00:00':'2018-04-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-04-01 00:00:00':'2018-05-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-05-01 00:00:00':'2018-06-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-06-01 00:00:00':'2018-07-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-07-01 00:00:00':'2018-08-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-08-01 00:00:00':'2018-09-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-09-01 00:00:00':'2018-10-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-10-01 00:00:00':'2018-11-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-11-01 00:00:00':'2018-12-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-12-01 00:00:00':'2019-01-01 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_18_monthly.png')

#Plotting 2018 weekly per month
plt.plot(dat_series_18['2018-01-01 00:00:00':'2018-01-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-02-01 00:00:00':'2018-02-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-03-01 00:00:00':'2018-03-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-04-01 00:00:00':'2018-04-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-05-01 00:00:00':'2018-05-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-06-01 00:00:00':'2018-06-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-07-01 00:00:00':'2018-07-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-08-01 00:00:00':'2018-08-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-09-01 00:00:00':'2018-09-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-10-01 00:00:00':'2018-10-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-11-01 00:00:00':'2018-11-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-12-01 00:00:00':'2018-12-07 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_18_weekly.png')


#Plotting 2018 daily per month Wednesday
plt.plot(dat_series_18['2018-01-10 00:00:00':'2018-01-11 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-02-07 00:00:00':'2018-02-11 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-03-07 00:00:00':'2018-03-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-04-07 00:00:00':'2018-04-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-05-04 00:00:00':'2018-05-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-06-09 00:00:00':'2018-06-10 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-07-04 00:00:00':'2018-07-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-08-08 00:00:00':'2018-08-09 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-09-05 00:00:00':'2018-09-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-10-10 00:00:00':'2018-10-11 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-11-07 00:00:00':'2018-11-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-12-05 00:00:00':'2018-12-06 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_18_daily_weekday.png')

#Plotting 2018 daily per month Sunday 
plt.plot(dat_series_18['2018-01-07 00:00:00':'2018-01-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-02-04 00:00:00':'2018-02-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-03-04 00:00:00':'2018-03-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-04-01 00:00:00':'2018-04-02 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-05-06 00:00:00':'2018-05-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-06-03 00:00:00':'2018-06-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-07-01 00:00:00':'2018-07-02 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-08-05 00:00:00':'2018-08-06 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-09-02 00:00:00':'2018-09-03 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-10-07 00:00:00':'2018-10-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-11-04 00:00:00':'2018-11-05 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_18['2018-12-02 00:00:00':'2019-12-03 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_18_weekend.png')


#Plotting 2019

plt.plot(dat_series_19['Forecasting Error'])
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_19.png')


#Plotting 2019 monthly 
plt.plot(dat_series_19['2019-01-01 00:00:00':'2019-02-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-02-01 00:00:00':'2019-03-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-03-01 00:00:00':'2019-04-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-04-01 00:00:00':'2019-05-01 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-05-01 00:00:00':'2019-06-01 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_19_monthly.png')

#Plotting 2019 weekly per month
plt.plot(dat_series_19['2019-01-01 00:00:00':'2019-01-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-02-01 00:00:00':'2019-02-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-03-01 00:00:00':'2019-03-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-04-01 00:00:00':'2019-04-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-05-01 00:00:00':'2019-05-07 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_19_weekly.png')


#Plotting 2019 daily per month Wednesday
plt.plot(dat_series_19['2019-01-02 00:00:00':'2019-01-03 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-02-06 00:00:00':'2019-02-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-03-06 00:00:00':'2019-03-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-04-03 00:00:00':'2019-04-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-05-01 00:00:00':'2019-05-02 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_19_daily_weekday.png')

#Plotting 2019 daily per month Sunday 
plt.plot(dat_series_19['2019-01-06 00:00:00':'2019-01-07 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-02-03 00:00:00':'2019-02-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-03-03 00:00:00':'2019-03-04 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-04-07 00:00:00':'2019-04-08 00:00:00']['Forecasting Error'].values)
plt.plot(dat_series_19['2019-05-05 00:00:00':'2019-05-06 00:00:00']['Forecasting Error'].values)
plt.xlabel('Time')
plt.ylabel('Day-ahead Forecasting Error')
plt.show()
plt.savefig('Forecasting_Err_19_weekend.png')






