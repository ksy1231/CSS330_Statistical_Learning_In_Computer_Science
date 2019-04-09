#- Imports:

import numpy as np
from scipy.stats import hypergeom
from scipy.stats import fisher_exact


#- My Fisher's exact method function returning the p-value when the 
#  alternative hypothesis is p1 > p2:

def fisher_exact_greater(table):
    '''Calculate the p-value for a contingency table for H_a "greater".
    
    Uses the algorithm from zyBook Section 4.2.  Row and column totals
    are assumed fixed.  The null hypothesis is p1 = p2 where p1 is 
    dependent on table[0][0] and p2 is dependent on table[1][0]. The
    alternative hypothesis is p1 > p2.
    
    A list of all possible tables is created by changing the first row,
    first column element in the contingency table through all possible
    values, which is assumed to be 0 to the minimum between the sum of
    the first row and the sum of the first column.  All values in the
    contingency table are assumed to be integers zero or greater.
    
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
    
    #- Calculate probabilities of all possible tables where the number of
    #  correctly guessed cans equals or is greater than the input table.
    possible_tables_probab = []
    max_X = np.min([total_row0, total_col0])
    N = total_row0 + total_row1
    m = total_col0
    k = total_row0
    
    for X in range(max_X + 1):
        if X >= table_array[0,0]:
            probab = hypergeom.pmf(X, N, m, k)
            possible_tables_probab.append(probab)
            
    #- Return sum of probabilities of the greater than more unlikely
    #  tables:
    return np.sum(possible_tables_probab)


#  P-value for the teacher correctly identified 7 samples from cans:

print("For correctly identified 7 samples from cans:")
print("  Original contingency table p-value (SciPy):" + \
        str(fisher_exact([[7, 3], [4, 6]], alternative='greater')[1]))  
print("  Original contingency table p-value (JWL): " + \
        str(fisher_exact_greater([[7, 3], [4, 6]])))  


#  P-value for the teacher correctly identified 8 samples from cans:

print("For correctly identified 8 samples from cans:")
print("  Original contingency table p-value (SciPy):" + \
        str(fisher_exact([[8, 2], [3, 7]], alternative='greater')[1]))  
print("  Original contingency table p-value (JWL): " + \
        str(fisher_exact_greater([[8, 2], [3, 7]]))) 
        

#===== end file =====