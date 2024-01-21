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
        
        
for i in range(exp.size):
    if(exp[i]) > 0:
        print("exp[%d] = %.f" % (i, exp[i]))
        
for i in range(exp.size):
    if(exp[i]) > 8:
        print("exp[%d] = %.f" % (i, exp[i]))
        

        
for i in range(exp.size):
    if(math.isnan(exp[i])):
        exp[i] = statistics.median(exp)
        print("exp[%d] = %.f" % (i, exp[i]))
        

print('\n')
exp_mean_recalculated = statistics.mean(exp)
print("Recalculated mean is: ", exp_mean_recalculated)
print(exp)


for i in range(exp.size):
    if(exp[i])<0:
        exp[i] = abs(exp[i])
        print("exp[%d] = %.f" % (i, exp[i]))
        
print('\n')
exp_mean_recalculated2 = statistics.mean(exp)
print('\n')
print("Recalculated mean1 is: ", exp_mean_recalculated2)
print(exp)

salary = salaryMDS.iloc[:, 1].values
print(salary)

print("Size of the salary is: ", salary.size)
print("Mean of the salary is: ", statistics.mean(salary))
print("Median of the salary is: ", statistics.median(salary))

for i in range(salary.size):
    if(math.isnan(salary[i])):
        salary[i] = statistics.median(salary)
        print("salary[%d] = %.f" % (i, salary[i]))
        
print(salary)
        
print("Recalculated Mean of the salary is: ", statistics.mean(salary))
print("Recalculated Median of the salary is: ", statistics.median(salary))




#Importing Invalid Titannic Data .csv file
TitanicDS = pd.read_csv('Invalid_Titanic_Data1.csv')
age = TitanicDS.iloc[:, 4].values
print(age)

for i in range(age.size):
    if(age[i])<0:
        print("age[%d] = %.f" % (i, age[i]))
        
        
for i in range(age.size):
    if(age[i])<0:
       age[i] = abs(age[i])
       print("age[%d] = %.f" % (i, age[i]))
       
print(age)


# Another Data validationa nd Missing Data Problem/ solution
# From a randomly generated dataset

import numpy as np

rowCount = 10
colCount = 2

randomDS = np.zeros((rowCount, colCount), dtype = int)
print(randomDS)

"""
Populate the first column with i.i.d. random variables N(16, 100) for 
somulating height, and the second column with i.i.d. random(25, 225)
for simulating weight. Here(Mean, Variance)
"""


if(age[i])<0:
        age[i] = abs(age[i])
        print("age[%d] = %.f" % (i, age[i]))
    
height = randomDS[:, 0]
weight = randomDS[:, 1]

for i in range(rowCount):
    height[i] = np.random.normal(loc = 16, scale = 10, size = 1)
    weight[i] = np.random.normal(loc = 25, scale = 15, size = 1)

print('\n')
for i in range(rowCount):
    if(weight[i])<=0:
        weight[i] = abs(weight[i])+50
    elif(height[i])<=0:
        height[i] = abs(height[i])+20
        
        
print('\n After cleaning: ')
print('Cleaned/preprocessed weight: ', weight)
print('Cleaned/preprocessed height: ', height)