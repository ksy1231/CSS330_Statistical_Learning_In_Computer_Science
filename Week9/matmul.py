#- matmul is same as dot
import numpy as np
a = np.array([[1, 0],
              [0, 1]])
b = np.array([1, 2])
print(np.matmul(a, b))