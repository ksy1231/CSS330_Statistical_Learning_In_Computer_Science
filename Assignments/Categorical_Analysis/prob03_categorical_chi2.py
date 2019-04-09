#------------------------------------------------------------------------------
# Function to do a chi-squared test for a 2 population/category contingency
# table.
#
# Code by Soo Yun Kim
# March 6, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   4.3.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
import scipy.stats
from contingency import expected  #the function I wrote
from scipy.stats import chi2
from scipy.stats import fisher_exact


#- Function to calculate the p-level using a chi-squared test:

def chi2_contingency(table, diag=False):
    """Calculate the p-value using a chi-squared test.
    
    Methodology from:  ZyBook, Statistics for Data Analytics, 2016,
    Section 4.3.  
    
    Input Parameter:
        table : list
            Contains r elements, where each element represents a row
            in the contingency table and each row is a list of c elements.
            
    Return Value:
        P-value.
    """
    table_array = np.array(table)
    ta_nrow = np.shape(table_array)[0]  #number of rows in input table
    ta_ncol = np.shape(table_array)[1]  #number of columns in input table
    
    dof = (ta_nrow - 1) * (ta_ncol - 1)  #degrees of freedom
    
    #Chi-squared statistic:
    chi2_statistic = np.sum(\
        (table_array - np.array(expected(table)) ) **2 / \
        np.array(expected(table)))
           
    #- Calculate and return p-value:
    return 1.0 - chi2.cdf(chi2_statistic, dof)


#- P-value using zyBook Participation Activity 4.2.5 data:

if __name__ == "__main__":
    input_table = [[374, 2629,], [73, 1219]]
    print("P-value from SciPy stats chi2_contingency:")
    print("  " + str(scipy.stats.chi2_contingency(input_table)[1]))
    print("P-value from my chi2_contingency:")
    print("  " + str(chi2_contingency(input_table)))
    print("Fisher exact p-value (Scipy): ")
    print("  " +str(fisher_exact(input_table, alternative='two-sided')[1]))

 
#===== end file =====  