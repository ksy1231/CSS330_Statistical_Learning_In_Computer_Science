#-----------------------------------------------------------------------------
# ANOVA statistics.
#
# Code by Soo Yun Kim
# February 6, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   2.4.
#-----------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import f


#- Function to calculate the F-statistic:

def f_statistic(levels, diag=False):
    """Calculate the F-statistic.

    Input Parameters:
        levels : list 
            List where each element is a NumPy array that is the samples 
            for that level.
            
        diag : bool
            If True, diagnostic messages will print prior to return.  If
            False, no such messages will print to the console.

    Return Value:
        float : F-statistic.
        
    Notes:
    * Does not use the scipy.stats f object or f_oneway function.
    """
    #- Calculate number of levels:
    k = len(levels)

    #- Calculate overall mean and overall sample size:
    xall = levels[0]
    for ilevel in levels[1:]:
        xall = np.concatenate((xall, ilevel))
    xall_bar = np.mean(xall)
    n = np.size(xall)

    #- Calculate mean squares between groups:
    MSB = 0.0
    for ilevel in levels:
        n_i = np.size(ilevel)
        x_i_bar = np.mean(ilevel)
        MSB += n_i * (x_i_bar - xall_bar)**2
    MSB = MSB / (k - 1)

    #- Calculate mean squares within groups:
    MSW = 0.0
    for ilevel in levels:
        x_i_bar = np.mean(ilevel)
        MSW += np.sum((ilevel - x_i_bar)**2)
    MSW = MSW / (n - k)

    if diag:
        print("MSB: " + str(MSB))
        print("MSW: " + str(MSW))
        print("n-k: " + str(n-k))

    return MSB / MSW


#- Compare function result with what is expected if compared to f_oneway.

if __name__ == "__main__":
    A = np.array([6, 4, 8, 12, 3, 4, 14, 2, 4])
    B = np.array([16, 2, 17, 11, 3, 7, 19, 8])
    C = np.array([23, 4, 9, 21, 19])

    k = 3   #number of levels
    n = 22  #total number of samples
    dfb = k - 1  #between-group or numerator degrees of freedom
    dfw = n - k  #within-group or denominator degrees of freedom

    print("f_statistic f-statistic: " + \
        str(f_statistic([A, B, C], diag=True)))
    print("p-value using above f-statistic: " + \
        str(1.0 - f.cdf(f_statistic([A, B, C]), dfb, dfw)))


#===== end file =====