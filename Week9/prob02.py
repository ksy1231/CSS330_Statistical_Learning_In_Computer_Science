#- Imports:

import numpy as np
from numpy.linalg import inv

A = np.array([[3, 6, -2],
              [6, 12, -4],
              [-1, 3, 7]])
try:
    Ainv = inv(A)
except np.linalg.linalg.LinAlgError:
    print("LinAlgError")


#===== end file =====