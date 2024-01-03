# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:55:27 2024

@author: ISMAIL
"""

import pandas as pd
import statistics

data1 = [1, 2, 3, 4, 4, 5, 7, 9]

#Mean method in python
data1_mean = statistics.mean(data1)

print('Mean of data1 is = ', data1_mean)
print("Mean is : %.2f" % (data1_mean))  #.2f means that it will take 2 digits after decimal
print("Mean is : %.3f" % (data1_mean))  #.3f means that it will take 3 digits after decimal
print("Mean is : %.4f" % (data1_mean))  #.4f means that it will take 4 digits after decimal
print("Mean is : %.5f" % (data1_mean))  #.5f means that it will take 5 digits after decimal
print("Mean is : %.6f" % (data1_mean))  #.6f means that it will take 6 digits after decimal
print("\n")

#Median method in python
data1_Median = statistics.mode(data1)
print("Median of Data_1 is: ", data1_Median)

#Mode method in python
data1_Mode = statistics.mode(data1)
print("Mode of Data_1 is: ", data1_Mode)

#Standard deviation in python
data1_StDev = statistics.stdev(data1)
print("Standard Deviation of Data_1 is: ", data1_StDev)

#Variance of a data in pyhton
data1_variance = statistics.variance(data1)
print("Vairance of data1 is: ", data1_variance)
                               
