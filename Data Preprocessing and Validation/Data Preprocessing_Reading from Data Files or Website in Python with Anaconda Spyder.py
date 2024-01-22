# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:08:11 2024

@author: ISMAIL
"""

import pandas as pd
import numpy as np
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

expVector2 = dataMatrix[:, 0]
salVector2 = dataMatrix[:, 1]
print(expVector2)
print(salVector2)

print('Size of Experience Vector= ', expVector.size)
print('Size of Experience Vector2= ', expVector2.size)

print('Size of Experience Vector = ', expVector.size)
print('Size of Experience Vector2 = ', expVector2.size)


for i in range(expVector.size):
    print("expVector[%d] = %.f " % (i, expVector[i]))
    
for i in range(expVector2.size):    
    if (expVector[i])<2:
        print("expVector2[%d] = %.f " % (i, expVector2[i]))
        
        
for i in range(expVector2.size):
    if(expVector2[i])>8:
        print("expVector2[%d} = %.f " % (i, expVector2[i]))
        
    
titanicDS = pd.read_csv("Dummy_Titanic_Data.csv")
print(titanicDS)


titanicDM = titanicDS.iloc[:, 0:9].values
print(titanicDM)


survival_status = titanicDS.iloc[:, 0].values
print('Survival Status: ', survival_status)

ticket_class = titanicDS.iloc[:, 1].values
print("Ticket Class: " ,ticket_class)

age = titanicDS.iloc[:, 4]
print('age= ', age)
