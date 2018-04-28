import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt 

import sys
from io import StringIO

import os 
import numpy as np
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn import utils
from UserPrediction import knn_predict


pd.set_option('display.float_format', lambda x: '%.6f' % x)

def test_knn_predict():
    
    # Check function output is a tuple 
    actualstdout = sys.stdout
    sys.stdout = StringIO()
    dg = knn_predict(3,0.5,7)
    sys.stdout = actualstdout
    sys.stdout.write(str(dg))
    sys.stdout.flush()
    assert type(dg) == np.ndarray, "Output should be dtype numpy ndarray. Please check function for error"
    
    # Check the path of the file containing the train and test data
    if os.path.exists('afm_datafile_v3.csv') is True:
        pass
    else:
        raise Exception('atm_datafile_v3.csv contains the training and testing dataset. Please check current working directory.')
    
    
    # try oddball input
    a = float(3)
    try:
        knn_predict(a,0.5,7)
    except Exception:
        pass
    else: 
        raise Exception('float object (k) cannot be interpreted as an integer. Check function for TypeError')
        
    # try oddball input: ph out of range
    a = 16
    try:
        knn_predict(3,0.5,a)
    except Exception:
        pass
    else: 
        raise Exception('pH is out of range. Check function for AssertionError')    
    
     # try oddball input: conc out of range
    a = 3.0
    try:
        knn_predict(3,a,7)
    except Exception:
        pass
    else: 
        raise Exception('Concentration is out of range. Check function for AssertionError')
    
    sys.stdout = sys.__stdout__  
    return
	