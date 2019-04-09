#------------------------------------------------------------------------------
# Function that returns the probability for a discrete random variable that 
# follows the hypergeometric distribution.
#
# Code by Soo Yun Kim
# March 6, 2019
#
# Notes:
# * Written for Python 3.6.
#------------------------------------------------------------------------------


#- Imports:

import math
import numpy as np
from scipy.stats import hypergeom
from scipy.special import factorial

def choose(n,r):
    return factorial(n) / factorial(n-r) - factorial(r)
    
    def hypergeom(x,b,r,k):
        range_x = [np.max([0,k-r]), np.min([k,b])]
        if (x < range_x[0]) or (x > range_x[1]):
            return 0.0
        else:
            return float(choose(b,x) * choose(r,k-x) /choose(b+r, k))
hypergeom(3,7,8,5)
hypergeom.pmf(3,15,7,5)

#- Function following the Pishro-Nik algorithm:

def hypergeometric(X, N, n, k):
    '''Calculate Hypergeometric Probability.
    
    Uses the Pishro-Nik algorithm from Pishro-Nik Section 3.1.5.  

    Input Parameter:
            X : integer
                number of correctly identified smaples from data
                
            N : integer
                total samples
            
            n : integer
                total samples from data
                
            k : integer
                number of guesses (correct and not) 
                that a sample comes from data     
                
    Return:
        PMF
    '''
    nX = math.factorial(n) / (math.factorial(n - X) * math.factorial(X))
    NnkX = math.factorial(N - n) / (math.factorial((N - n) - (k - X)) * \
            math.factorial(k- X))
    Nk = math.factorial(N) / (math.factorial(N - k) * math.factorial(k))
    pmf = nX * NnkX / Nk
    
    return pmf
    
# Probability the teacher correctly identified 7 samples from cans:

N = 20 #total orange juice samples
m = 11 #total orange juice samples from a can
n = 9  #total orange juice samples from a bottle
k = 10 #number of guesses (correct and not) that a sample comes from a can
X = 7 #number of correctly identified orange juice smaples from a can
probab = hypergeom.pmf(X, N, m, k)

print("P(X=" + str(X) + "): " + str(probab))
print("P(X=" + str(X) + "): " + str(hypergeometric(X, N, m, k)))

# Probability the teacher correctly identified 6 samples from bottles:

N = 20 #total orange juice samples
m = 11 #total orange juice samples from a can
n = 9  #total orange juice samples from a bottle
k = 10 #number of guesses (correct and not) that a sample comes from a bottle
X = 6  #number of correctly identified orange juice smaples from a bottle
probab = hypergeom.pmf(X, N, n, k)

print("P(X=" + str(X) + "): " + str(probab))
print("P(X=" + str(X) + "): " + str(hypergeometric(X, N, n, k)))


#===== end file =====