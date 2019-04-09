#- Imports:

import numpy as np

#- Function to calculate the expected contingency table:

def expected(table, diag=False):
    '''Calculate the expected contingency table given an input table.
    
    Input Parameter:
        table : list
            Contains r elements, where each element represents a row
            in the contingency table and each row is a list of c elements.
            
    Return Value:
        A list of the same structure and size as table containing the
        expected contingency table values.
    '''
    table_array = np.array(table)
    ta_nrow = np.shape(table_array)[0]  #number of rows in input table
    ta_ncol = np.shape(table_array)[1]  #number of columns in input table
    
    #- Create working array:  This array contains an extra column and
    #  row to hold the totals:
    working_array = np.zeros( (ta_nrow + 1, ta_ncol + 1), dtype = 'd')
    
    working_array[0:ta_nrow, 0:ta_ncol] = table_array[:,:]
    
    #- Fill row and column totals:
    for irow in range(np.shape(working_array)[0]):
        working_array[irow,-1] = np.sum(working_array[irow, 0:-1])
        
    for icol in range(np.shape(working_array)[1]):
        working_array[-1,icol] = np.sum(working_array[0:-1,icol])
    
    #- Calculate expected values:  Equals the row total times the column
    #  total divided by the overall total for each element in the
    #  contingency table.
    output_array = np.zeros( (ta_nrow, ta_ncol), dtype = 'd')
    
    for irow in range(ta_nrow):
        for icol in range(ta_ncol):
            output_array[irow,icol] = \
                working_array[irow,-1] * working_array[-1,icol] / \
                working_array[-1,-1]    
    
    return output_array.tolist()
    

#- Created expected contingency table using zyBook Participation Activity
#  4.3.3 data:

if __name__ == "__main__":
    input_table = [[40, 217,],
                   [34, 1350]]
    print("Input contingency table:")
    print("  " + str(input_table))
    print("Expected contingency table:")
    print("  " + str(expected(input_table)))


#===== end file =====