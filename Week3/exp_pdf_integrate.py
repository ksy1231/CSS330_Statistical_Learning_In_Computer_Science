import numpy as np
from scipy.integrate import quad

def myexp(x, mylambda=0.1):
    return mylambda * np.exp(-mylambda * x)
    
p1 = quad(myexp, 0, 1)
p2 = quad(myexp, 1, 10)
p3 = quad(myexp, 10, np.inf)

print(p1[0])
print(p2[0])
print(p3[0])