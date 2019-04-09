import numpy as np

def variance(data):
    """
    avg_data = np.mean(data)
    sum = 0.0
    for i in range(np.size(data)):
        sum += (data[i] - avg_data)**2
    return sum / (np.size(data) - 1.0)
    """
    return np.sum((np.array(data) - np.mean(data))**2) \
            / (np.size(data) - 1.0)