#------------------------------------------------------------------------------
# Multiple regression.
#
# Code by Soo Yun Kim
# March 8, 2019
#
# Notes:
# * Written for Python 3.4.
# * Data from:  ZyBook, Statistics for Data Analytics, 2016, Section 6.1,
#   R-Practice 6.1.1 in this section.  Data and comments are directly copied
#   from the zyBook.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from sklearn.linear_model import LinearRegression
from numpy.linalg import inv
from numpy.linalg import lstsq


#- Data: Y, X1, X2, and X3 should all have the same number of elements:

#+ Body fat (%):
Y = np.array([11.9, 22.8, 18.7, 20.1, 12.9, 21.7, 27.1, 25.4, 21.3, 19.3, 
              25.4, 27.2, 11.7, 17.8, 12.8, 23.9, 22.6, 25.4, 14.8, 21.1])

#+ Triceps skinfold thickness (mm):
X1 = np.array([19.5, 24.7, 30.7, 29.8, 19.1, 25.6, 31.4, 27.9, 22.1, 25.5, 
                 31.1, 30.4, 18.7, 19.7, 14.6, 29.5, 27.7, 30.2, 22.7, 25.2])

#+ Midarm circumference (cm)
X2 = np.array([29.1, 28.2, 37, 31.1, 30.9, 23.7, 27.6, 30.6, 23.2, 24.8, 
               30, 28.3, 23, 28.6, 21.3, 30.1, 25.7, 24.6, 27.1, 27.5])

#+ Thigh circumference (cm)
X3 = np.array([43.1, 49.8, 51.9, 54.3, 42.2, 53.9, 58.5, 52.1, 49.9, 53.5, 
               56.6, 56.7, 46.5, 44.2, 42.7, 54.4, 55.3, 58.6, 48.2, 51])


#- Using scikit-learn package's LinearRegression model:

#+ vstack turns a 1-D array into a column vector and hstack lines up
#  the three column vectors next to each other.  For more info., see
#  https://stackoverflow.com/a/5954747:
X = np.hstack((np.vstack(X1), np.vstack(X2), np.vstack(X3)))

model = LinearRegression().fit(X, Y)

#+ Attributes with a trailing underscore (e.g., coef_, intercept_) are
#  estimated from the sample and are set after running the fit method.
#  See https://github.com/rasbt/python-machine-learning-book/blob/master/
#  faq/underscore-convention.md:
print("-> Scikit-learn's LinearRegression:")
print("  Intercept:          " + str(model.intercept_))
print("  Coefficient for X1: " + str(model.coef_[0]))
print("  Coefficient for X2: " + str(model.coef_[1]))
print("  Coefficient for X3: " + str(model.coef_[2]))
print("  R^2 coefficient:    " + str(model.score(X, Y)))


#- Using a pre-written generalized least squares function:  To the previous
#  value of X we need to add a column of ones to the left because the factor
#  in front of the \beta_0 term of the multiple linear regression model is
#  a one (the other \beta_n terms are multiplied by the Xni values for the
#  ith sample, where n=1,2,3; see zyBook for more on this notation):

X = np.hstack((np.vstack(np.ones(np.size(X1))), X))
coeff = lstsq(X, Y)

print("\n-> Numpy's least square function:")
print("  Intercept:          " + str(coeff[0][0]))
print("  Coefficient for X1: " + str(coeff[0][1]))
print("  Coefficient for X2: " + str(coeff[0][2]))
print("  Coefficient for X3: " + str(coeff[0][3]))


#- Using Chamberlain's linear algebra solution to the least squares method:

coeff = np.matmul(np.matmul(inv(np.matmul(X.T, X)), X.T), Y)

print("\n-> Chamberlain's linear algebra least squares method:")
print("  Intercept:          " + str(coeff[0]))
print("  Coefficient for X1: " + str(coeff[1]))
print("  Coefficient for X2: " + str(coeff[2]))
print("  Coefficient for X3: " + str(coeff[3]))


#===== end file =====