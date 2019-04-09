#-----------------------------------------------------------------------------
# Wilcoxon rank-sum method.
#
# Code by Soo Yun Kim
# February 27, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   3.3.  The data is copied from Participation Activity 3.3.4 in this
#   section.
# * This data in this problem is fake. 
#-----------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import norm


#- Function to calculate the W statistic:

def wilcoxon(x, y, diag=False):
    """Calculate the W statistic using the Wilcoxon rank-sum method.

    The p-value is obtained assuming the W statistic approximates a
    normal distribution, which will be true for samples sizes typically
    at least 10.  The p-value is assumed to be one-tailed; multiply the
    result by two if you want a two-tailed value.

    Input Parameters:
        x : array
            One sample of data.

        y : array
            Another sample of data.

        diag : boolean
            If True, print out diagnostics.

    Return Parameters:
        W-statistic and p-value.  Each are scalars.
    """
    #- Create data array:
    data = np.concatenate((x, y))
    group = np.array(['x']*np.size(x) + ['y']*np.size(y))


    #- Sort the data and calculate rankings:  The NumPy argsort command
    #  gives the indices that would sort the given array:

    indices = np.argsort(data)
    data = data[indices]                          #in sorted order
    group = group[indices]                        #in sorted order

    #ranking start at 1 w/o averaging of duplicate data:
    ranking_orig = np.arange(np.size(data)) + 1


    #- Calculate ranking with averaging of duplicate data:  isclose is 
    #  used to accommodate for floating point inprecision:

    ranking = np.zeros(np.size(data), dtype='d')  
    for i in range(np.size(data)):
        is_dupes = np.isclose(data[i], data)
        ranking[i] = np.sum(is_dupes * ranking_orig) \
                   / float(np.sum(is_dupes))


    #- Calculate various parameters:

    W_x = np.sum(np.where(group == 'x', ranking, 0.0))
    W_y = np.sum(np.where(group == 'y', ranking, 0.0))
    W = np.minimum(W_x, W_y)

    n1 = np.size(x)
    n2 = np.size(y)
    mu_W = n1 * (n1 + n2 + 1) / 2.0
    S_W = np.sqrt(n1 * n2 * (n1 + n2 + 1) / 12.0)

    Z = (W - mu_W) / S_W
    p_value = norm.cdf(Z)
    alpha = 0.05


    #- Printing diagnostics:

    if diag:
        print('Rankings: ' + str(ranking))
        print('W_x: ' + str(W_x))
        print('W_y: ' + str(W_y))
        print('W: ' + str(W))
        print('mu_W: ' + str(mu_W))
        print('S_W: ' + str(S_W))
        print('Z: ' + str(Z))
        print('p_value: ' + str(p_value))
        print('Reject H0?' + str(p_value* 2.0 <alpha))

    return W, p_value


if __name__ == "__main__":
    a  = np.array([4, 8, 5, 6, 7, 9, 7, 8, 5])  #hours' sleep men
    c1 = np.array([9, 3, 4, 5, 6, 6, 7, 8, 7])  #hours' sleep women

    print("Wilcoxon using hours of sleep of men and women data:")
    wilcoxon(a, c1, diag=True)


#===== end file =====