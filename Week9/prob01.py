#- Imports:

import numpy as np
from numpy.linalg import inv
from numpy.linalg import solve

A = np.array([[1, 2, 3],
              [2, 1, 3],
              [3, 2, 1]])
              
x = np.array([1, 1, 1])

b = np.matmul(A, x)
print(b)

Ainv = inv(A)

X = np.matmul(Ainv, b)
print(X)

X = solve(A, b)
print(X)


#===== end file =====