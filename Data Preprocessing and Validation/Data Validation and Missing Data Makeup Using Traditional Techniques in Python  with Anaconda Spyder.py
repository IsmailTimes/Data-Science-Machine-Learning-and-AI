# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:25:26 2024

@author: ISMAIL
"""

import pandas as pd
import statistics
import math



salaryMDS = pd.read_csv('Invalid_Salary_Data1.csv')
print(salaryMDS)


exp = salaryMDS.iloc[:, 0].values
salary = salaryMDS.iloc[:, 1].values


exp_mean = statistics.mean(exp)
exp_median = statistics.median(exp)

print("Mean of Experience is: ", exp_mean)
print("Median of Experience is: ", exp_median)


print('Experience size: ', exp.size)

for i in range(exp.size):
    print("exp[%d] = %.f" % (i, exp[i]))
    
for i in range(exp.size):    
    if(exp[i]) < 0:
        print("exp[%d] = %.f" % (i, exp[i]))
