# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 20:36:12 2024

@author: ISMAIL
"""

import pandas as pd
import numpy as np

titanicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print(titanicDS)

sl_No = titanicDS.iloc[:, 0].values
print(sl_No)

#col12 contains : for all rows and [1,2] means second and 3rd column
col12 = titanicDS.iloc[:, [1,2]].values   
print(col12)


#col124 contains : for all rows and [1, 2, 4] means second, 3rd column and 5th column
col124 = titanicDS.iloc[:, [1, 2, 3]].values
print(col124)

#col12347 contains : for all rows and [1, 2, 3, 4, 7] means second, 3rd, 4th, 5th & 8th column
col12347 = titanicDS.iloc[:, [1, 2, 3, 4, 7]].values
print(col12347)

#col12347 contains : for all rows and [1:7] means second to 8th column
cole1_7 = titanicDS.iloc[:, 1:7].values
print(cole1_7)


#Here iloc[0] means all vlaues of row 1 where 0 means 1st row
passenger1 = titanicDS.iloc[0]
print(passenger1)

#Here iloc[1] means all vlaues of row 2 where 0 means 1st row
passenger2 = titanicDS.iloc[1]
print(passenger2)

passenger2436 = titanicDS.iloc[2435]
print(passenger2436)


#To get the data of the top 10 passengers
passengerTop10 = titanicDS.head(10)
print(passengerTop10)

#Or another way
passenger1_10 = titanicDS.iloc[0:10]
print(passenger1_10)


#To get the data of passenger 1 &2
passenger12 = titanicDS.iloc[[0,1]]
print(passenger12)


#To get the data of 1, 2, 100
passenger12100 = titanicDS.iloc[[0, 1, 99]]
print(passenger12100)







#To get first two rows's 1, 2 & 8 columns
passenger12x128 = titanicDS.iloc[[0 ,1], [0, 1, 7]]
print(passenger12x128)
