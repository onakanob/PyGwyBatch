# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:30:47 2018

@author: sarth
"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

pd.set_option('display.float_format', lambda x: '%.6f' % x)

# Reading the DataFile
df = pd.read_csv('afm_datafile_v3.csv')

# Deciding parameters
test_size = 0.2 # Test size
k = 5 # Number of neighbors
weights = 'distance' # uniform or distance based weights for knn

# Concentration is in nM in Original dataset - converting to uM for making better plots
df['concentration'] = df['concentration'] * 1e6


#------------------------------- NO USER INPUT BELOW THIS --------------------------

# Train-Test split
df_train, df_test = train_test_split(df, test_size = test_size, random_state = 15)

# Converting label type from continuous to Multiclass for knn
lab_enc = preprocessing.LabelEncoder()
encoded_ROD = lab_enc.fit_transform(df_train['ROD'])
utils.multiclass.type_of_target(encoded_ROD)

# KNN fit here
knn = KNeighborsClassifier(n_neighbors = k, weights = weights)
knn.fit(df_train[['concentration', 'pH']], encoded_ROD)

#Predict Ratio of order to disorder (ROD) for test data set
testing_pred = knn.predict(df_test[['concentration', 'pH']])

#Display the predictions for Ratio of Order to Disorder for Test set
print ('The disorder value prediction is: ' + str(testing_pred))


#Assign disorder level based on the predicted value above
def disorder_level(disorder):
    level = []
    for i in disorder:
        if i == 0:
            level += ['completely disordered']

        elif 0 < i <= 1:
            level += ['highly disordered']

        elif i > 1:
            level += ['completely ordered']
    
    return level


#Conver disorder number to a categoty
#Printing the predictions for Ratio of Order to Disorder for Test set
disorder = disorder_level(testing_pred)
print ('Disorder level of your sample is: ' + str(disorder))

#disorder level of actual data
actual = disorder_level(np.array(df_test['ROD']))


# Calculating error
correct = 0 
for i in range(len(disorder)):
    if disorder[i] == actual[i]:
        correct += 1
    else:
        correct = correct

#calculating ratio of correct prediction to all predictions
correct_ratio = correct / len(disorder)

print ('The percent of correct prediction is: ' + str(correct_ratio))


# Plotting Training data set wrt to concentration, pH and ROD with 'Kind' as color levels
levels,labels = pd.factorize(df_train.Kind)
y = levels

plt.figure()
ax = Axes3D(plt.gcf())
ax.scatter(df_train.concentration, df_train.pH, df_train.ROD, zdir = 'z', c = y, s = 100, depthshade = False, edgecolor = 'k')
ax.set_xlabel('Peptide Concentration (uM)')
ax.set_ylabel('pH')
ax.set_zlabel('Order-Disorder Ratio')
ax.set_title('Training Data', fontsize = 15)
plt.savefig('Order_Disorder_ratio', dpi = 300)

# Plotting Actual ROD vs Predicted values for specific concentration and pH from KNN for Test data set
plt.figure()
ax = Axes3D(plt.gcf())
ax.scatter(df_test.concentration, df_test.pH, testing_pred, zdir = 'z', c = 'r', marker = '*', s = 70, depthshade = False, label = 'Prediction')
ax.scatter(df_test.concentration, df_test.pH, df_test.ROD, zdir = 'z', c = 'b', marker = 'o', s = 100, depthshade = False, label = 'Actual', edgecolor = 'k')
ax.set_xlabel('Peptide Concentration (uM)')
ax.set_ylabel('pH')
ax.set_zlabel('Order-Disorder Ratio')
ax.set_title('Testing Data vs Prediction', fontsize = 15)
ax.legend(loc = 'best')
plt.savefig('testingdata_vs_prediction', dpi = 300)


