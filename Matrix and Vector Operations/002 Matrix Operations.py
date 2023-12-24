# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:32:09 2023

@author: ISMAIL
"""

import numpy as np #importing numpy and naming it as np


matrix1 = [[8,4,2], [6,1,5]]
matrix2 = [[3,10,4], [5,6,1]]

print("Matrix 1= " ,matrix1)
print("Matrix 2= " ,matrix2)


#Transpose of a matrix
print("\n")
print(np.transpose(matrix1))    #Row == Col, Col==Row


#Addition of two Matrix
matrix3 = np.matrix(matrix1) + np.matrix(matrix2)
print("\n")
print(matrix3)


#Matrix Substraction
matrix4 = np.matrix(matrix1) - np.matrix(matrix2)
print("\n")
print(matrix4)


#Multiplying matrix by a constant
print("\n", 2 * np.matrix(matrix1)) #Multiplying all elements by 2


#Doubling Matrix elements
print(2*matrix1)


#Matrix Multiplication
matrix_a = [[5,1,6], [0,8,-2]]
matrix_b = [[2], [3], [4]]
matrix5 = np.matrix(matrix_a) * np.matrix(matrix_b)
print("\n", matrix5)



#Inverse of 2x2 Matrix
matrix_x = [[4,7], [2,6]]
matrix_inv = np.linalg.inv(matrix_x)    #Only for 2x2 matrix
print("\n", matrix_inv) 


#Inverse of 3x3 Matrix
matrix_e = [[1,0,0],[-5, 1, 0], [0, 0, 1]]  #for 3x3 Matrix
matrix_inv_e = np.linalg.inv(matrix_e)
print("\n", matrix_inv_e)

#print("\nHello World!")
#print("\nI am learning Python for DS, ML, AI, DL")
#print("\nHappy Data Science")