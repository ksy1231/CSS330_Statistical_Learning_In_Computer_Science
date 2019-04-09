#------------------------------------------------------------------------------
# Problem 2
# Write a function that calculates each of the values in the zyBook Table 
# 6.2.1 Analysis of Variance Table in Section 6.2.  As input, the function 
# should accept a 2-D NumPy array of predictor values where each column is all 
# the sample values for one predictor variable. Each row represents the values 
# of all predictor variables for one sample.  The function should also accept 
# as input a 1-D NumPy array of response values where each element is the 
# response for one sample.  Have the return value be a single list that 
# contains all ten values in the table. Confirm you obtain the zyBook 
# Participation Activity 6.2.3 results when running it on the data from the 
# zyBook R-Practice 6.1.1.
#
# Code by Soo Yun Kim
# March 13, 2019
#
# Notes:
# * Written for Python 3.4.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from numpy.linalg import inv
from scipy.stats import f


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

X = np.hstack((np.vstack(X1), np.vstack(X2), np.vstack(X3)))

def overall_anova(Xin, Yin):
    '''
        Xin : 2-D array
        Yin : 1-D array
    '''
    n = np.shape(Xin)[0] #- Number of samples
    p = np.shape(Xin)[1] #- Number of regression parameters

    X = np.hstack((np.vstack(np.ones(n)), Xin))
    Y = Yin
    
    #- Estimated regression coefficients: As a 1_D array and duplicated
    #  so each row gives all the estimated regression coefficients:
    beta = np.matmul(np.matmul(inv(np.matmul(X.T, X)), X.T), Y)
    beta_n = np.reshape(np.resize(beta, np.size(beta)*n), (n,np.size(beta)))
    
    #- Fitted response values (Yhat) and sum squares:
    Yhat = np.sum(beta_n * X, axis=1)
    SSR = np.sum((Yhat - np.mean(Yin))**2)
    SSE = np.sum((Yin - Yhat)**2)
    SSTO = np.sum((Yin - np.mean(Yin))**2)
    
    #- Mean square:
    MSR = SSR / (p - 1)
    MSE = SSE / (n - p)
    
    #- F-stat
    f_statistic = MSR / MSE
    p_value = 1.0 - f.cdf(f_statistic, p-1, n-p)
    
    return SSR, p-1, MSR, f_statistic, p_value, SSE, n-p, MSE, SSTO, n-1

anova_values = overall_anova(X, Y)  
print("SSR:         " + str(anova_values[0]))
print("DOF:         " + str(anova_values[1]))
print("MSR:         " + str(anova_values[2]))
print("F-statistic: " + str(anova_values[3]))
print("p-value:     " + str(anova_values[4]))
print("SSE:         " + str(anova_values[5]))
print("DOF:         " + str(anova_values[6]))
print("MSE:         " + str(anova_values[7]))
print("SSTO:        " + str(anova_values[8]))
print("DOF:         " + str(anova_values[9]))


#===== end file =====