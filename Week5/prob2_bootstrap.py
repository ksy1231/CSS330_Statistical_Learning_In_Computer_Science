#- Imports:

import numpy as np
import matplotlib.pyplot as plt


#- Data:

male = np.array([245,200,145,180,250,205,195,170,140,170], dtype='d')
female = np.array([165,120,170,190,195,120,170,140,130,150], dtype='d')


#- Calculate difference for each bootstrap resample the difference in the
#  mean of male and female values:

results = np.zeros(10000, dtype='d')
for i in range(np.size(results)):
    data_male = np.random.choice(male, np.size(male), replace=True)
    data_female = np.random.choice(female, np.size(female), replace=True)
    results[i] = np.mean(data_male) - np.mean(data_female)
    
    
#- Plot histogram:
xbar = np.mean(male) - np.mean(female)  #difference in sample means
num_bins = int(np.sqrt(np.size(results)))  #ZyBooks Section 1.3
plt.figure(1)
n, bins, patches = plt.hist(results, num_bins, density=True)
plt.plot([xbar, xbar], [0, np,max(n)], 'o-')  #plot xbar on distribution
plt.ylabel('PDF')
plt.xlabel('Difference in mean Weight Between Men and Wom [1bs]')
plt.title('Bootstrap Test')
plt.savefig('bootstrap_3_2_2.png')