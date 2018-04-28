import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from skimage import morphology, color, segmentation, feature, filters, io
import cv2

from ImageSeparationFunc import order_disorder_separation
from ImageSegmentationFunc import convert_to_grayscale
from ImageSegmentationFunc import seg_random_walker
from ImagePreprocessing import bckgrnd_correc_rect


import sys
from io import StringIO


I1_test = np.loadtxt('tdj_grbp5_1um_1hr_3rd_020717.001.txt')
gh = bckgrnd_correc_rect(I1_test,10,200)
plt.close()
gray_I1 = convert_to_grayscale(gh)
plt.close()
trial_t = seg_random_walker(gray_I1,0.15)
plt.close()
plt.close()
plt.close()

def test_order_disorder_separation():
    
    # try oddball input
    
    # try pandas loaded image data    
    datas = pd.read_csv('tdj_grbp5_1um_1hr_3rd_020717.001.txt', sep=" ")
    try:
        order_disorder_separation(datas,40,25)
    except Exception:
        pass
    else: 
        raise Exception('Image data must be numpy ndarray. Check function for error')
        
    # try float percentile number     
    per_fl = float(40)
    try:
        order_disorder_separation(trial_t,per_fl,10)
    except Exception:
        pass
    else: 
        raise Exception('Percentile input must be int dtype. Check function for error') 
    
    # try float size number     
    size_fl = float(10)
    try:
        order_disorder_separation(trial_t,40,size_fl)
    except Exception:
        pass
    else: 
        raise Exception('size input must be int dtype. Check function for error') 
        
    # try percentile number larger than 100     
    per_fl_b = 120
    try:
        order_disorder_separation(trial_t,per_fl_b,10)
    except Exception:
        pass
    else: 
        raise Exception('Percentile input is bounded between 0 and 100. Check function for error')
        
    #check expected outputs
    
    
    # Check function output is a tuple 
    actualstdout = sys.stdout
    sys.stdout = StringIO()
    vb = order_disorder_separation(trial_t,40,10)
    plt.close()
    plt.close()
    plt.close()
    plt.close()
    sys.stdout = actualstdout
    sys.stdout.write(str(vb))
    sys.stdout.flush()
    assert type(vb) == tuple, "Function output should be a tuple. Please check function for expected error"
    #sys.stdout = sys.__stdout__
    
    # Check Image outputs are still grayscale
    for i in range(0,3):
        assert ((vb[i] < float(0)).any() == False) & ((vb[i] > float(1)).any() == False), "Filtered, ordered and disordered images dtype should be bounded between 0 and 1, and be a float. Please check function for expected error"
    
    # Check other outputs are np.float64
    for i in range(3,7): 
        assert type(vb[i]) == np.float64, "Check calculation of 4 output parameters, as they should be a dtype np.float64. Check Function for error"
    
    sys.stdout = sys.__stdout__    
    return