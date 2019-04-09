#-----------------------------------------------------------------------------
# Paired t-test function.
#
# Code by Johnny Lin
# January 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   2.3.
#-----------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import t
from scipy.stats import ttest_rel


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
    x1_array = np.array(x1)
    x2_array = np.array(x2)

    if np.size(x1_array) != np.size(x2_array):
        raise ValueError("dimensions mismatch for paired t-test")

    diffs = x1_array - x2_array   #sample differences
    dbar = np.mean(diffs)         #mean of sample differences
    mu_d = 0.0                    #hypothesized pop. mean of differences
    s_d = np.std(diffs, ddof=1)   #std. dev. of sample differences
    n = np.size(x1_array)         #sample size
    dof = n - 1                   #degrees of freedom

    t_statistic = (dbar - mu_d) / (s_d / np.sqrt(n))
    p_value = t.cdf(t_statistic, dof) * 2.0

    if diag:
        print("t-statistic: " + str(t_statistic))
        print("dof: " + str(dof))
        print("p-value: " + str(p_value))

    return p_value < alpha


#- Compare function result with what is expected if compared to ttest_rel:

#  + Caffeine data is from R-Practice 2.3.1 in the zyBooks.  The "data
#    [is] from the 'The Effect of Different Dosages of Caffeine on
#    Endurance Performance Time', International Journal of Sports
#    Medicine (http://www.ncbi.nlm.nih.gov/pubmed/7657415). The data set 
#    gives the endurance times (in minutes) of 9 athletes when given a 
#    caffeine dose of 5 milligrams and 13 milligrams."  Column 1 is for 
#    the 5 mg dose and column 2 for the 13 mg dose:

if __name__ == "__main__":
    caffeine = np.array([ \
        [35.05, 36.20],
        [44.50, 46.48],
        [73.25, 69.47],
        [66.20, 70.54],
        [42.47, 37.55],
        [52.10, 58.33],
        [57.17, 66.35],
        [63.20, 79.12],
        [85.15, 59.30]])

    alpha = 0.05
    print("Reject H0?: " + \
          str(h0_mu_d_zero(caffeine[:,0], caffeine[:,1], alpha, diag=True)))
    print(ttest_rel(caffeine[:,0], caffeine[:,1]))


#===== end file =====
