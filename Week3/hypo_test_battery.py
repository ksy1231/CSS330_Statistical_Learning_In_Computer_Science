import numpy as np
from scipy.stats import t

x = np.array([19, 18, 22, 20, 16, 25])
xbar = np.mean(x)
s = np.std(x, ddof=1)
mu0 =21.5

t_statistic = (xbar - mu0) / (s / np.sqrt(n))
p_value = t.cdf(t_statistic, dof)

print("Sample mean: " + str(xbar))
