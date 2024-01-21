# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 18:55:06 2024

@author: ISMAIL
"""
import pandas as pd
import statistics
import numpy as np

#Import Invalid Salary Data 1 csv file
invalidDS = pd.read_csv("Invalid_Salary_Data1.csv")

print(invalidDS)

exp = invalidDS.iloc[:, 0].values
salary = invalidDS.iloc[:, 1].values


print('\n')
exp_mean = statistics.mean(exp)
exp_median = statistics.median(exp)
print('Mean of experience: ', exp_mean)
print('Median of experience: ', exp_median)


print('\n')
salary_mean = statistics.mean(salary)
salary_median = statistics.median(salary)
print('Mean of the Salary: ', salary_mean)
print('Median of the Salary: ', salary_median)

validatedDS = invalidDS

import sklearn     
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')
imputer = imputer.fit(validatedDS[:, 0:2])
validatedDS[:, 0:2] = imputer.transform(validatedDS[:, 0:2])




# Assuming 'validatedDS' is your dataset
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
validatedDS[:, 0:2] = imputer.fit_transform(validatedDS[:, 0:2])

