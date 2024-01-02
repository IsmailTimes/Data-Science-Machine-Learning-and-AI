# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 20:43:13 2023

@author: ISMAIL
"""

import pandas as pd

salaryDS = pd.read_csv('Dummy_Salary_Data.csv')
print(salaryDS)

exp = salaryDS.iloc[:, 0].values
salary = salaryDS.iloc[:, 1].values

print(exp)
print(salary)

titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print(titanicDS)


sl_No = titanicDS.iloc[:, 0].values
print(sl_No)


survival_Status = titanicDS.iloc[:, 1].values
print(survival_Status)


ticket_Class = titanicDS.iloc[:, 2].values
print(ticket_Class)


gender = titanicDS.iloc[:, 3].values
age = titanicDS.iloc[:, 4].values
spouse_siblings_abroad = titanicDS.iloc[:, 5].values
parents_children_abroad = titanicDS.iloc[:, 6].values
ticket_fare =  titanicDS.iloc[:, 7].values


print(gender)
print(age)
print(spouse_siblings_abroad)
print(parents_children_abroad)
print(ticket_fare)



#Importing the Titanic Excel data file 
titanic3DS = pd.read_excel('Titanic_Data3.xls')
print(titanic3DS)


