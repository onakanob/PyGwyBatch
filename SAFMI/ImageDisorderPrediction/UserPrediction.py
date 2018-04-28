# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 13:30:47 2018

@author: sarth
"""

import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn import utils


pd.set_option('display.float_format', lambda x: '%.6f' % x)


def knn_predict(k, concentration, pH):
    """
    Predict disorder by training a knn algorithm with
    existing peptide data. Prediction is based on the set
    of pH and concentration the user provides. 
    
    Args:
        k: int, number of neighbors
        concentration: a float or int, in uM
        pH: a float or int
    
    Return:
        Disorder
    
    Raises:
        Error when the input is out of range
        
    """
    
    assert 1 < k < 50, 'k must an integer within the given range'
    
    assert 0.1 > float(concentration) or float(concentration) < 2.0, 'Concentration is out of range.'
    
    assert 1.0 < float(pH) < 14.0, 'pH out of range.'
    
    # Reading the DataFile containing training and testing set
    df = pd.read_csv('afm_datafile_v3.csv')

    # Deciding parametes
    weights = 'distance' # uniform or distance based weights for knn

    # Create a dataframe based on user inputs
    X_dict = {'concentration': [concentration], 'pH': [pH]}
    predict_X = pd.DataFrame(X_dict)


    # Converting label type from continous to Multiclass for knn
    lab_enc = preprocessing.LabelEncoder()
    encoded_ROD = lab_enc.fit_transform(df['ROD'])
    utils.multiclass.type_of_target(encoded_ROD)

    # KNN fit here
    knn = KNeighborsClassifier(n_neighbors = k, weights = weights)
    knn.fit(df[['concentration', 'pH']], encoded_ROD)

    # Predicting Ratio of order to disorder (ROD) for test data set
    testing_pred = knn.predict(predict_X[['concentration', 'pH']])
    
    if testing_pred == 0:
        disorder_level = 'completely disordered'
    
    elif 0 < testing_pred < 1:
        disorder_level = 'highly disordered'
        
    elif testing_pred > 1:
        disorder_level = 'completely ordered'
        
    #Printing the predictions for Ratio of Order to Disorder for Test set 
    print ('Disorder level of your sample is: ' + disorder_level)
    
    return testing_pred




if __name__ == '__main__':
    """main function to run functions based on user interaction"""
    
    print ('---AFM Peptide Image Disorder Prediction---')
    print ('Hello! Welcome to AFM Peptide Image Disorder Prediction!')
    
    #asks for user's pH and concentration
    print('Please enter a pH value from 1 to 14')
    pH_user = input('pH: ')

    print('Please enter concentration from 0.1 to 2 (uM)')
    conc_user = input('Concentration: ')

    print('Please enter the number of neighbors to compare.')
    k_user = int(input('k (must be integer from 1 to 50): '))
    

    knn_predict(k_user, conc_user, pH_user)
    
    