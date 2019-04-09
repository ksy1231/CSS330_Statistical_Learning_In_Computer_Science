#------------------------------------------------------------------------------
# Linear algebra.
#
# Code by Soo Yun Kim
# March 8, 2019
#
# Notes:
# * Written for Python 3.4.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from numpy.linalg import inv
from numpy.linalg import solve


#- Main program:

# ICA Question 1:

A = np.array([[3, 6, -2],
              [-2, 9, 3],
              [-1, 4, 8]])
              
x = np.array([4, 3, -2])

b = np.array([34, 13, -8])

print("-> Part a:")
print("A = \n" + str(A))
print("x = \n" + str(x))
print("b = \n" + str(b))
print("Ax = " + str(np.matmul(A, x)))

Ainv = inv(A)

print("x from A^{-1}b = " + str(np.matmul(Ainv, b)))

print("x from solve = " + str(solve(A, b)))


# ICA Question 2:

print("\n-> Part b:")
A = np.array([[3, 6, -2],
              [6, 12, -4],
              [-1, 3, 7]])
try:
    Ainv = inv(A)
except np.linalg.linalg.LinAlgError:
    print("Singular A matrix = \n" + str(A))
    print("Using inv results in LinAlgError")
    

#===== end file =====