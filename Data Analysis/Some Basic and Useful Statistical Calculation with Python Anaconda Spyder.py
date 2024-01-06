# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:55:27 2024

@author: ISMAIL
"""

import pandas as pd
import statistics
import numpy as np

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
data1_StDev = np.std(data1)
print("Standard Deviation of Data_1 is: ", data1_StDev)

#Variance of a data in pyhton
data1_variance = statistics.variance(data1)
print("Vairance of data1 is: ", data1_variance)


#Importing the salary.csv data set
salaryDS = pd.read_csv('Dummy_Salary_Data.csv')
print(salaryDS)        


exp = salaryDS.iloc[:, 0].values
salary = salaryDS.iloc[:, 1].values

print('Experience: ', exp)
print("Salary: ", salary)
exp_mean = statistics.mean(exp)
exp_median = statistics.median(exp)
exp_mode = statistics.mode(exp)
exp_stdev = statistics.stdev(exp)
exp_variance = statistics.variance(exp)

print("Mean of Experience is: ", exp_mean)
print("Median of Experience is: ", exp_median)
print("Mode of Experience is: ", exp_mode)
print("Standard Deviation of Experience is: ", exp_stdev)
print("Variance of Experience is: ", exp_variance)

print("Salary: ", salary)

salary_mean = statistics.mean(salary)
salary_median = statistics.median(salary)
salary_mode = statistics.mode(salary)

#salary_stdev = statistics.stdev(salary)


# Assuming 'salary' is a NumPy array or another iterable with numpy.int64 elements
salary_list = np.array(salary).tolist()

# Now calculate the standard deviation using the converted list
salary_stdev = statistics.stdev(salary_list)




salary_variance = statistics.variance(salary)

print('\n')
print('Mean of the salary is: ', salary_mean)
print('Median of the salary is: ', salary_median)
print('Mode of the salary is: ', salary_mode)
print('Standard Deviation of the salary is: ', salary_stdev)
print('Variance of the salary is: ', salary_variance)



# Importing the Titanic .csv file
print('\n')
titadicDS = pd.read_csv('Dummy_Titanic_Data.csv')
print(titadicDS)

age = titadicDS.iloc[:, 4].values

print('\n')
age_stdev = statistics.stdev(age)
print('St Deviation of  age is: ', age_stdev)

age_variance = statistics.variance(age)
print(age_variance)

print('\n')
ticket_fare = titadicDS.iloc[:, 7]
ticket_fare_stdev = statistics.stdev(ticket_fare)
print("St devations of ticket fare is : ", ticket_fare_stdev)

print('\n')
ticket_fare_variance = statistics.variance(ticket_fare)
print("Variance of ticket fare is: ", ticket_fare_variance)
