#-----------------------------------------------------------------------------
# Program to solve a cars problem using Kruskal-Wallis.
#
# Code by Soo Yun Kim
# February 27, 2019
#
# The null hypothesis is the muA = muB = muC.  The alternative hypothesis 
# is that at least one pair of mus do not equal.  muA is the population mean 
# for the Model A number of defects and muB and muC are the same for Models
# B and C, respectively.  The null hypothesis is not rejected.
#
# Notes:
# * Written for Python 3.6.
# * Algorithms based on:  ZyBook, Statistics for Data Analytics, 2016.
#-----------------------------------------------------------------------------

#- Imports:

import numpy as np
from scipy.stats import kruskal
from scipy.stats import chi2


#- Data and parameters:

placebo = np.array([6, 4, 2, 2, 1])  
aspirin = np.array([4, 5, 6, 5, 6])   
new_painkiller = np.array([6, 5, 7, 8, 7])   
alpha = 0.05


#- Statistical metrics:

g = 3       #number of groups
df = g - 1  #degrees of freedom
h_statistic, scipy_p_value = kruskal(placebo, aspirin, new_painkiller)


#- Function to calculate the H statistic:

def kruskal_wallis_solution(input_list, diag=False):
    '''
        input_list : list
                    Each element of the list is an array of one group's worth
                    of data
    '''
    
    data = np.concatenate((input_list))
    
    group = []
    for i in range(np.size(input_list)):
        group += [i]*np.size(input_list[i])
    group = np.array(group)
    
    
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
                   
    
    #- Calculate R_i, the sum of ranks for each group:
    
    R_i = []
    for i in range(len(input_list)):
        R_i.append(np.sum(np.where(group==i, ranking,0.0)))
    R_i = np.array(R_i)
    
    N =np.size(data)
    temp = 0.0
    for i in range(len(input_list)):
        n_i = np.size(input_list[i])
        temp += (R_i[i]**2) / n_i
    temp *= 12.0/(N*(N+1))
    H = temp - (3.0 * (N+1))
    
    df = len(input_list)-1
    p_value = 1.0 - chi2.cdf(H, df)
                  
    return H, p_value
    
def kruskal_wallis(x, y, z, diag=False):
    """Calculate the H statistic using Kruskal-Wallis.

    Input Parameters:
        x : array
            One sample of data.

        y : array
            Another sample of data.
            
        z : array
            The other sample of data.    

        diag : boolean
            If True, print out diagnostics.

    Return Parameters:
        h_statistic.  This is scalar.
    """
    #- Create data array:
    data = np.concatenate((x, y, z))
    group = np.array(['x']*np.size(x) + ['y']*np.size(y) + ['z']*np.size(z))
    
    
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
    
    n1 = np.size(x)
    n2 = np.size(y)
    n3 = np.size(z)
    N = n1 + n2 + n3
    
    R_x = np.sum(np.where(group == 'x', ranking, 0.0))
    R_y = np.sum(np.where(group == 'y', ranking, 0.0))
    R_z = np.sum(np.where(group == 'z', ranking, 0.0))
    
    h_statistic = (12.0 / (N * (N + 1))) * \
                  (R_x**2 / n1 + R_y**2 / n2 + R_z**2 / n3) - \
                  (3 * (N + 1))
                  
    return h_statistic


#- Print stuff out:
if __name__ == "__main__":
    print("My version of Kruskal-Wallis using zyBook Table 3.4.1 data:")
    kruskal_wallis([placebo, aspirin, new_painkiller], diag=True)
    print("scipy.stats Kruskal-Wallis using zyBook Table 3.4.1 data:")
    print('H: ' + str(kruskal(placebo, aspirin, new_painkiller)[0]))
    print('p-value: ' + str(kruskal(placebo, aspirin, new_painkiller)[1]))

print('H-statistic: ' + \
      "{:<8.4f}".format(kruskal_wallis_solution(placebo, aspirin, 
      new_painkiller, diag=True)))
print('H-statistic: ' + "{:<8.4f}".format(h_statistic))


#===== end file =====