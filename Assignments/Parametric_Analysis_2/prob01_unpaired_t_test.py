#-----------------------------------------------------------------------------
# Paired t-test function.
#
# Code by Soo Yun Kim
# February 6, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   2.3.
#-----------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import t
from scipy.stats import ttest_ind


#- Function:

def h0_mu_d_zero(x1, x2, alpha, diag=False):
    """Conduct paired t-test.

    Conducts a paired t-test to see whether the p-value is less than
    the significance level, for $H_0: mu_d=0$ and $H_a: mu_d ne 0$.
    Because the alternative hypothesis is that $mu_d ne 0$, this is a
    two-tailed test.

    Input Parameters:
        x1 : list or array
            First sample
            
        x2 : list or array
            Second sample
            
        alpha : float
            The significance level $alpha$.  Ex. 95% is 0.05.

        diag : bool
            If True, diagnostic messages will print prior to return.  If
            False, no such messages will print to the console.

    Return Value:
        boolean : True if $H_0$ is rejected and False otherwise.
        
    Notes:
    * Does not use the scipy.stats ttest_rel function.
    """
    
    diffs = np.mean(x1) - np.mean(x2)    #sample differences
    s1 = np.std(x1, ddof=1)              #std. dev. of sample differences
    s2 = np.std(x2, ddof=1)
    sq_s1 = s1**2
    sq_s2 = s2**2
    n1 = np.size(x1)                     #sample size
    n2 = np.size(x2)
    dof = n1 + n2 - 2                    #degrees of freedom

    t_statistic = diffs / np.sqrt((sq_s1/n1) + (sq_s2/n2))
    p_value = t.cdf(t_statistic, dof) * 2.0

    if diag:
        print("t-statistic: " + str(t_statistic))
        print("dof: " + str(dof))
        print("p-value: " + str(p_value))

    return p_value < alpha


#- Compare function result with what is expected if compared to ttest_rel:

if __name__ == "__main__":
    A = np.array([6, 4, 8, 12, 3, 4, 14, 2, 4])
    B = np.array([16, 2, 17, 11, 3, 7, 19, 8])

    alpha = 0.05
    print("Reject H0?: " + \
          str(h0_mu_d_zero(A, B, alpha, diag=True)))
    print(ttest_ind(A, B))


#===== end file =====