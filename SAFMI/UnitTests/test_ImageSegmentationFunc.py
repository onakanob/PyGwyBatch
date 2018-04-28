import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from ImageSegmentationFunc import convert_to_grayscale
from ImageSegmentationFunc import seg_random_walker
from ImagePreprocessing import bckgrnd_correc_rect


I1_test = np.loadtxt('tdj_grbp5_1um_1hr_3rd_020717.001.txt')
gh = bckgrnd_correc_rect(I1_test,10,200)
plt.close()
gray_I1 = convert_to_grayscale(gh)
plt.close()

def test_convert_to_grayscale():
     
    # try pandas loaded image data    
    datag = pd.read_csv('tdj_grbp5_1um_1hr_3rd_020717.001.txt', sep=" ")
    try:
        convert_to_grayscale(datag)
    except Exception:
        pass
    else: 
        raise Exception('Image data must be numpy ndarray. Check function for error')
 
    
    #check expected outputs
    chg = convert_to_grayscale(I1_test)
    plt.close()
    assert type(chg) == np.ndarray, "Function output should be numpy ndarray. Please check function for expected error"
    
    #check max value of grayscale image output
    assert ((chg < float(0)).any() == False) & ((chg > float(1)).any() == False), "Min and max value of grayscaled ndimage should be between 0 and 1. Check normalization within function" 
    
    return


def test_seg_random_walker():
    
    # try oddball input
    
    # try pandas loaded image data    
    datas = pd.read_csv('tdj_grbp5_1um_1hr_3rd_020717.001.txt', sep=" ")
    d = float(0.20)
    try:
        seg_random_walker(datas,d)
    except Exception:
        pass
    else: 
        raise Exception('Image data must be numpy ndarray. Check function for error')
        
    # try marker_threshold number larger than 1     
    mar_b = 1.2
    try:
        seg_random_walker(gray_I1, mar_b)
    except Exception:
        pass
    else: 
        raise Exception('marker_threshold input is bounded between 0 and 1. Check function for error')
      
    # try a non-grayscale image
    I1_test = np.loadtxt('tdj_grbp5_1um_1hr_3rd_020717.001.txt')
    try:
        seg_random_walker(I1_test, d)
    except Exception:
        pass
    else: 
        raise Exception('Image input must be grayscale meaning, array values are bounded between 0 and 1. Check function for error')
    
    # try integer for marker_threshold     
    s = int(0.2)
    try:
        seg_random_walker(I1_test, s)
    except Exception:
        pass
    else: 
        raise Exception('size input must be int dtype. Check function for error')
    
    # Check function output is a tuple
    fb = seg_random_walker(gray_I1,0.15)
    plt.close()
    plt.close()
    plt.close()
    assert type(fb) == np.ndarray, "Function output should be a numpy ndarray. Please check function for expected error"
    
    # Check Image output is still grayscale
    assert ((fb[0] < float(0)).any() == False) & ((fb[0] > float(1)).any() == False), " Segmented image dtype should be bounded between 0 and 1, and be a float64. Please check function for expected error"
    
    return