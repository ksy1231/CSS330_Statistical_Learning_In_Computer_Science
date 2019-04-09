import numpy as np
from scipy.stats import t

melons = [7.72, 9.58, 12.38, 7.77, 11.27, 8.80, 11.10, 7.80, 10.17, 6.00]
melons = np.array(melons)
xbar = np.mean(melons)
s_x = np.std(melons, ddof=1)
alpha = 0.05
n = np.size(melons)

t_statistic = t.ppf(alpha / 2.0, n -1)
confid_lower = xbar - abs(t_statistic) * s_x / np.sqrt(n)
confid_upper = xbar + abs(t_statistic) * s_x / np.sqrt(n)

print("T-statistic: ", t_statistic)
print("Confid. interval: ", [confid_lower, confid_upper])