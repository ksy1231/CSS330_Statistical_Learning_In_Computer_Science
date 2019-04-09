# Student t-distribution Percent Point Function
from scipy.stats import t

# define probability
p1 = 0.9
p2 = 0.95
p3 = 0.975
p4 = 0.995

df1 = 5
df2 = 10
df3 = 15

def t_distribution(p, df):
    """Calculate confidence interval for a t-distribution

        https://machinelearningmastery.com/critical-values-for-statistical-hypothesis-testing/
        
        Positional Input Parameters:
            p : one-tailed or two-tailed
                Must all be numerical.

            df : degrees of freedom
                 Must all be numerical.
        
        Returns:
             Critical values for common significance levels
    """
    value = t.ppf(p, df)
    return value

print(t_distribution(p1, df1))
print(t_distribution(p1, df2))
print(t_distribution(p1, df3))
print(t_distribution(p2, df1))
print(t_distribution(p2, df2))
print(t_distribution(p2, df3))
print(t_distribution(p3, df1))
print(t_distribution(p3, df2))
print(t_distribution(p3, df3))
print(t_distribution(p4, df1))
print(t_distribution(p4, df2))
print(t_distribution(p4, df3))