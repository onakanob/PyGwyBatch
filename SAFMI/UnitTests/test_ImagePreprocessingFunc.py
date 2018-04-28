import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

from ImagePreprocessingFunc import bckgrnd_correc_rect
from ImagePreprocessingFunc import bckgrnd_correc_sq
from ImagePreprocessingFunc import bckgrnd_correc_disk
from ImagePreprocessingFunc import convert_to_grayscale

I1_test = np.loadtxt('tdj_grbp5_1um_1hr_3rd_020717.001.txt')

def test_bckgrnd_correc_rect():
        
    #check expected outputs
    a = int(40)
    b = int(40)
    ch = bckgrnd_correc_rect(I1_test,a,b)
    assert type(ch) == np.ndarray, "Function output should be numpy ndarray. Please check function for expected error"
    
     # try pandas loaded image data    
    data = pd.read_csv('tdj_grbp5_1um_1hr_3rd_020717.001.txt', sep=" ")
    try:
        bckgrnd_correc_rect(data,a,b)
    except Exception:
        pass
    else: 
        raise Exception('Image data must be numpy ndarray. Check function for error')
        
    # try oddball input
    a = float(60)
    b = float(60)
    try:
        bckgrnd_correc_rect(I1_test,a,b)
        plt.close(1)
    except Exception:
        pass
    else: 
        raise Exception('Morphology.rectangle only takes int dtype for structuring dimensions. Check function for error')
        
    return



def test_bckgrnd_correc_sq():
     
    #check expected outputs
    b = int(100)
    ch = bckgrnd_correc_sq(I1_test,b)
    assert type(ch) == np.ndarray, "Function output should be numpy ndarray. Please check function for expected error"
    
     # try pandas loaded image data    
    dataq = pd.read_csv('tdj_grbp5_1um_1hr_3rd_020717.001.txt', sep=" ")
    try:
        bckgrnd_correc_sq(dataq,b)
    except Exception:
        pass
    else: 
        raise Exception('Image data must be numpy ndarray. Check function for error')
        
    # try oddball input
    a = float(60)
    try:
        bckgrnd_correc_sq(I1_test,a)
    except Exception:
        pass
    else: 
        raise Exception('Morphology.square only takes int dtype for structuring dimensions. Check function for error')

    return


def test_bckgrnd_correc_disk():
       
    #check expected outputs
    b = int(2)
    chs = bckgrnd_correc_disk(I1_test,b)
    plt.close(1)
    assert type(chs) == np.ndarray, "Function output should be numpy ndarray. Please check function for expected error"
    
     # try pandas loaded image data    
    datas = pd.read_csv('tdj_grbp5_1um_1hr_3rd_020717.001.txt', sep=" ")
    try:
        bckgrnd_correc_disk(datas,b)
        plt.close(1)
    except Exception:
        pass
    else: 
        raise Exception('Image data must be numpy ndarray. Check function for error')
        
    # try oddball input
    a = float(3)
    try:
        bckgrnd_correc_disk(I1_test,a)
    except Exception:
        pass
    else: 
        raise Exception('Morphology.disk only takes int dtype for structuring dimensions. Check function for error')  
    return


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
    assert type(chg) == np.ndarray, "Function output should be numpy ndarray. Please check function for expected error"
    
    #check min and max value of grayscale image output
    assert ((chg < float(0)).any() == False) & ((chg > float(1)).any() == False), "Min and max value of grayscaled ndimage should be between 0 and 1. Check normalization within function" 
    
    return

