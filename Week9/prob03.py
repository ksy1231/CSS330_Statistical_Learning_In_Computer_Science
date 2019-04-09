#- Imports:

import numpy as np
from sklearn.linear_model import LinearRegression
from numpy.linalg import inv
from numpy.linalg import lstsq

#- Data:

Y = np.array([11.9, 22.8, 18.7, 20.1, 12.9, 21.7, 27.1, 25.4, 21.3, 19.3, 
              25.4, 27.2, 11.7, 17.8, 12.8, 23.9, 22.6, 25.4, 14.8, 21.1])
X1 = np.array([19.5, 24.7, 30.7, 29.8, 19.1, 25.6, 31.4, 27.9, 22.1, 25.5, 
                 31.1, 30.4, 18.7, 19.7, 14.6, 29.5, 27.7, 30.2, 22.7, 25.2])
X2 = np.array([29.1, 28.2, 37, 31.1, 30.9, 23.7, 27.6, 30.6, 23.2, 24.8, 
               30, 28.3, 23, 28.6, 21.3, 30.1, 25.7, 24.6, 27.1, 27.5])
X3 = np.array([43.1, 49.8, 51.9, 54.3, 42.2, 53.9, 58.5, 52.1, 49.9, 53.5, 
               56.6, 56.7, 46.5, 44.2, 42.7, 54.4, 55.3, 58.6, 48.2, 51])

X = np.hstack((np.vstack(X1), np.vstack(X2), np.vstack(X3)))
model = LinearRegression().fit(X, Y)

print("-> Scikit-learn's LinearRegression:")
print("  Intercept:          " + str(model.intercept_))
print("  Coefficient for X1: " + str(model.coef_[0]))
print("  Coefficient for X2: " + str(model.coef_[1]))
print("  Coefficient for X3: " + str(model.coef_[2]))

X = np.hstack((np.vstack(np.ones(np.size(X1))), X))
coeff = lstsq(X, Y)

print("\n-> Numpy's least square function:")
print("  Intercept:          " + str(coeff[0][0]))
print("  Coefficient for X1: " + str(coeff[0][1]))
print("  Coefficient for X2: " + str(coeff[0][2]))
print("  Coefficient for X3: " + str(coeff[0][3]))

coeff = np.matmul(np.matmul(inv(np.matmul(X.T, X)), X.T), Y)

print("\n-> Chamberlain's linear algebra least squares method:")
print("  Intercept:          " + str(coeff[0]))
print("  Coefficient for X1: " + str(coeff[1]))
print("  Coefficient for X2: " + str(coeff[2]))
print("  Coefficient for X3: " + str(coeff[3]))


#===== end file =====