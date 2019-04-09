#------------------------------------------------------------------------------
# Problem 3
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
from scipy.stats import t


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

def indiv_t(Xin, Yin):
    n = np.shape(Xin)[0] #- Number of samples
    p = np.shape(Xin)[1] + 1 #- Number of regression parameters

    X = np.hstack((np.vstack(np.ones(n)), Xin))
    Y = Yin
    
    #- Estimated regression coefficients: As a 1_D array and duplicated
    #  so each row gives all the estimated regression coefficients:
    beta = np.matmul(np.matmul(inv(np.matmul(X.T, X)), X.T), Y)
    beta_n = np.reshape(np.resize(beta, np.size(beta)*n), (n,np.size(beta)))
    
    #- Fitted response values (Yhat) and sum squares:
    Yhat = np.sum(beta_n * X, axis=1)
    SSE = np.sum((Yin - Yhat)**2)
    
    #- Mean square error and standard errors of parameters:
    MSE = SSE / (n - p)
    se_beta = np.sqrt(MSE * np.diag(inv(np.matmul(X.T, X))))
    
    #- t-statistic and p-value:  This is a two-tailed test since Ha is the
    #  regression parameter is non-zero.  Because it's two-tailed, I find the
    #  negative t-statistic value whose CDF will give me the probability of 
    #  equally or more extreme values and then I double that probability 
    #  (since the t-distribution is symmetric):
    t_statistic = beta / se_beta
    t_statistic = -np.absolute(t_statistic)
    p_value = t.cdf(t_statistic, n - p) * 2.0
    
    #- Return values:
    return p_value
    
    
#- Run test using data from the zyBook
X = np.hstack((np.vstack(X1), np.vstack(X2), np.vstack(X3)))
p_values = indiv_t(X, Y)
print("Model includes X1, X2, X3:   " + str(p_values))
   
X = np.hstack((np.vstack(X1), np.vstack(X2)))
p_values = indiv_t(X,Y)
print("Model includes X1, X2:       " + str(p_values))


#===== end file =====