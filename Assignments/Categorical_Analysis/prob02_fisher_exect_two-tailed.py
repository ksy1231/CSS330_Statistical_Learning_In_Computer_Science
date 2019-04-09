#------------------------------------------------------------------------------
# Fisher exact test for the two-tailed alternative hypothesis.
#
# Code by Soo Yun Kim
# March 6, 2019
#
# Notes:
# * Written for Python 3.6.
# * Methodology from:  ZyBook, Statistics for Data Analytics, 2016, Section
#   4.2, Example 4.2.2.  The nomenclature for parameters and random variables
#   is from that Example.
# * See also https://en.wikipedia.org/w/index.php?title=Fisher%27s_exact_test&
#   oldid=881250945 (accessed February 21, 2019) for more details on the test.
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from scipy.stats import hypergeom
from scipy.stats import fisher_exact


#- My Fisher's exact method function returning the p-value when the 
#  alternative hypothesis is p1 != p2:

def two_tailed_fisher_exact(table):
    '''Calculate the p-value for a contingency table.
    
    Input Parameter:
            table : list
                Contains two elements, each element is a two-element list
                giving the row for the contingenct table.
                
    Return:
        The p-value for table.
    '''
    table_array = np.array(table)
    
    #- Totals by row and columns:
    total_row0 = np.sum(table_array[0,:])
    total_row1 = np.sum(table_array[1,:])
    total_col0 = np.sum(table_array[:,0])
    #total_col1 = np.sum(table_array[:,1])
    
    possible_tables_probab = []
    max_X = np.min([total_row0, total_col0])
    N = total_row0 + total_row1
    m = total_col0
    k = total_row0
    
    X = np.arange(max_X + 1)
    possible_tables_probab = hypergeom.pmf(X, N, m, k)
    observed_probab = hypergeom.pmf(table_array[0,0], N, m, k)
    
    #- Return sum of probabilities more extreme than the observed.
    more_extreme = possible_tables_probab <= observed_probab   
    return np.sum(possible_tables_probab * more_extreme) 
    
#- P-value for the Participation Activity 4.2.5 contingency table regarding
#  white, Union soldiers in the Civil War:

print("Fisher exact p-value (Scipy): " +  \
        str(fisher_exact([[374, 2629], [73, 1219]],
        alternative='two-sided')[1]))
print("Fisher exact p-value (JWL): " + \
        str(two_tailed_fisher_exact([[374, 2629], [73, 1219]])))  
        

#===== end file =====