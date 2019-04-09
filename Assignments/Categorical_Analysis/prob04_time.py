#------------------------------------------------------------------------------
# Use the time.time function do a simple timing of how long it takes 
# to do the calculation each way
#
# Code by Soo Yun Kim
# March 6, 2019
#
# Notes:
# * Written for Python 3.6.
# * See https://pythonhow.com/measure-execution-time-python-code/ 
#   (accessed March 6, 2019) for more details on the measurement.
#------------------------------------------------------------------------------

#- Imports:

import time
import scipy.stats
from scipy.stats import fisher_exact

input_table = [[24329, 25345,], [173342, 174623]]
print("Fisher exact p-value (Scipy): ")
start_time = time.time()
print("  " +str(fisher_exact(input_table, alternative='two-sided')[1]))
print("  " + str(time.time() - start_time) + " seconds")
print("P-value from SciPy stats chi2_contingency:")
start_time = time.time()
print("  " +str(scipy.stats.chi2_contingency(input_table)[1]))
print("  " + str(time.time() - start_time) + " seconds")

if __name__ == "__main__":
    input_table = [[24329, 25345,],
                   [173342, 174623]]
    start = time.time()
    scipy.stats.chi2_contingency(input_table)[1]
    end = time.time()
    print("Time for chi2_contingency : " + str(end - start))
    
    start = time.time()
    fisher_exact(input_table)[1]
    end = time.time()
    print("Time for Fisher's exact test : " + str(end - start))
