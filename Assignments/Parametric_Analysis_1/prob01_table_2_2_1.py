import numpy as np
from scipy.stats import t

one_tailed = np.array([0.1, 0.05, 0.025, 0.005])
two_tailed = one_tailed * 2.0
df_5 = t.ppf(one_tailed, 5)
df_10 = t.ppf(one_tailed, 10)
df_15 = t.ppf(one_tailed, 15)

row_titles = ["One-tailed", "Two-tailed", "df = 5", "df = 10", "df = 15"]
row_values = [one_tailed, two_tailed, df_5, df_10, df_15]

output = ''
for i in range(5):
    output += "{:<10}".format(row_titles[i])
    for j in range(np.size(one_tailed)):
        output +="{:10.3f}".format(row_values[i][j])
    output += '\n'

print(output)