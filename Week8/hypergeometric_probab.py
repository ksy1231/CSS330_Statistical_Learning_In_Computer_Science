#- Imports:

from scipy.stats import hypergeom


# Probability the teacher correctly identified 7 samples from cans:

N = 20 #total orange juice samples
m = 11 #total orange juice samples from a can
n = 9  #total orange juice samples from a bottle
k = 10 #number of guesses (correct and not) that a sample comes from a can
X = 7 #number of correctly identified orange juice smaples from a can
probab = hypergeom.pmf(X, N, m, k)

print("P(X=" + str(X) + "): " + str(probab))


# Probability the teacher correctly identified 6 samples from bottles:

N = 20 #total orange juice samples
m = 11 #total orange juice samples from a can
n = 9  #total orange juice samples from a bottle
k = 10 #number of guesses (correct and not) that a sample comes from a bottle
X = 6  #number of correctly identified orange juice smaples from a bottle
probab = hypergeom.pmf(X, N, n, k)

print("P(X=" + str(X) + "): " + str(probab))


#===== end file =====