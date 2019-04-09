import numpy as np
import scipy.stats

def confidence_interval(data, confidence=0.95):
    """Calculate a confidence interval

        Positional Input Parameters:
            data : array
                Must all be numerical.
            
            confidence : a static number for alpha
                        Must all be numerical.
        
        Returns:
             a 95% confidence interval for mu
    """
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m-h, m+h
    
data = [7.72, 9.58, 12.38, 7.77, 11.27, 8.80, 11.10, 7.80, 10.17, 6.00]
print(confidence_interval(data))