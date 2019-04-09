#------------------------------------------------------------------------------
# Multiple logistic regression model of spambase data.
#
# By Johnny Lin
# March 2019
#
# Notes:
# * Written for Python 3.6.
# * About the dataset:  http://archive.ics.uci.edu/ml/datasets/Spambase
#------------------------------------------------------------------------------


#- Imports:

import numpy as np
from sklearn.linear_model import LogisticRegression


#- Obtain data:

raw_data = np.genfromtxt('spambase.data.txt', delimiter=',')
free = raw_data[:,15]
credit = raw_data[:,19]
george = raw_data[:,26]
area = raw_data[:,27]  #"650" (area code) word percentage
Y = raw_data[:,-1]     #1=spam, 0=non-spam

#+ vstack turns a 1-D array into a column vector and hstack lines up
#  the three column vectors next to each other.  For more info., see
#  https://stackoverflow.com/a/5954747:
X = np.hstack((np.vstack(free), np.vstack(credit), np.vstack(george), 
                np.vstack(area)))
#X = raw_data[:,:-1]   #use all the attributes in the dataset


#- Create and train model using first half of data:

n = np.size(free)
half_idx = int(np.round(n / 2.0))
model = LogisticRegression().fit(X[:half_idx, :], Y[:half_idx])

print("Logistic regression intercept:   " + str(model.intercept_))
print("Logistic regression paramenters: " + str(model.coef_))


#- Predict using the last half of the data and evaluate how it did.  For
#  the predict_proba output, the oneth column contains the probability
#  the predicted response variable equals 1:

actual_Y = Y[half_idx:]
predicted_Y = model.predict(X[half_idx:, :])
predicted_Y_probab = model.predict_proba(X[half_idx:, :])[:,1]

percent_correct = \
    np.sum(np.isclose(actual_Y, predicted_Y)) / np.size(actual_Y) * 100
print("Percent correctly predicted (predict):        " + str(percent_correct))

percent_correct = \
    np.sum(np.isclose(actual_Y, (predicted_Y_probab >= 0.5) * 1)) / \
           np.size(actual_Y) * 100
print("Percent correctly predicted (predict_proba):  " + str(percent_correct))


#===== end file =====