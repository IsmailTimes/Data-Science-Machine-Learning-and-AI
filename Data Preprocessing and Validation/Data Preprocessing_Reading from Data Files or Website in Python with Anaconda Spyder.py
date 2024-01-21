# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:08:11 2024

@author: ISMAIL
"""

import pandas as pd
filelocation = "Dummy_Salary_Data.csv"
#filelocation = "Dummy_Salary_Data.csv"

datasetDS = pd.read_csv(filelocation)
print(datasetDS)

dataMatrix = datasetDS.iloc[:, 0:2].values
print('Data Matrix= ', dataMatrix)

expMatrix = datasetDS.iloc[:, 0:1].values
salMatrix = datasetDS.iloc[:, 1:2].values
print('Experiance Matrix= ', expMatrix)
print('Salary Matrix= ', salMatrix)

expVector = datasetDS.iloc[:, 0].values
salVector = datasetDS.iloc[:, 1].values
print('Experience Vector= ', expVector)
print('Salary Vector= ', salVector)

