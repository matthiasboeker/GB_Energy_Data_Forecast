#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:35:52 2020

@author: matthiasboeker
"""

lj_test_statistic_16 = model4_16_fit.test_serial_correlation('ljungbox')
lj_test_statistic_17 = model1_17_fit.test_serial_correlation('ljungbox')
lj_test_statistic_18 = model3_18_fit.test_serial_correlation('ljungbox')

lj_test_statistic_exog_16 = exog_16_model.test_serial_correlation('ljungbox')
lj_test_statistic_exog_17 = exog_17_model.test_serial_correlation('ljungbox')
lj_test_statistic_exog_18 = exog_18_model.test_serial_correlation('ljungbox')

#Ljung Box Test 
line = np.repeat(0.05, len(lj_test_statistic_16[0][1]))
plt.plot(lj_test_statistic_16[0][1])
plt.plot(lj_test_statistic_exog_16[0][1])
plt.ylabel('p-Values')
plt.xlabel('Lags')
plt.plot(line,linestyle='--')
plt.savefig('/Users/matthiasboeker/Documents/Uni/Seminar_Master_Grothe/Seminar_Tex/Images/Chapter_5/ljung_box_new.png')


line = np.repeat(0.05, len(lj_test_statistic_17[0][1]))
plt.plot(lj_test_statistic_17[0][1])
plt.plot(lj_test_statistic_exog_17[0][1])
plt.ylabel('p-Values')
plt.xlabel('Lags')
plt.plot(line,linestyle='--')
plt.show()


line = np.repeat(0.05, len(lj_test_statistic_18[0][1]))
plt.plot(lj_test_statistic_18[0][1])
plt.plot(lj_test_statistic_exog_18[0][1])
plt.ylabel('p-Values')
plt.xlabel('Lags')
plt.plot(line,linestyle='--')
plt.show()

plt.plot(lj_test_statistic17[0][1])
plt.plot(lj_test_statistic18[0][1])
plt.plot(lj_test_statistic_exog_16[0][1])
plt.plot(lj_test_statistic_exog_16[0][1])


acf()