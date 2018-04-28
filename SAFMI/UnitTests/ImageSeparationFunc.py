# -*- coding: utf-8 -*-
"""
Created on Thu Mar 08 20:02:09 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def order_disorder_separation(image, percentile, size):
    
    """
    Seperates the input image into order and disorder regions 
    using percentile_filter from scipy.ndimage.
    This function will also provide parameters 
    such as order-diorder ratio, order percentage, disorder percentage 
    and total percent coverage from the separated images.
    
    Args:
        image: segmented image, numpy array
        percentile: float
        size: size of the separation filter, int
    
    Returns:
        filt_img: numpy array 
        I_ordered: float 
        I_disordered: float 
        order_disorder_ratio: float  
        percent_ordered: float  
        percent_disordered: float  
        percent_coverage: float 

    Raises:
        Errors when input datatype is wront
        Error when percentile is out of range.
    
    """

    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # Checking the right data type for the percentile
    assert type(percentile) == int, ('Wrong data type', 'percentile must be an integer')
    
    assert 0 <= percentile <= 100, ('Out of range', 'Percentile value must be between 0 and 100')    

    # Checking the right data type for the size
    assert type(size) == int, ('Wrong data type', 'size must be an integer')
    
    # Using percentile filter to filter image into two labels - 0 and 1 
    filt_img = ndimage.percentile_filter(image, percentile, size, mode='reflect')

    
    # creating a boolean array of all the labels - True = label == 1 and False = label == 0
    q = filt_img == 1
    
    # creating empty arrays similar to input image
    I_ordered = np.zeros_like(image)
    I_disordered = np.zeros_like(image)
    
    # Assigning values for ordered and disordered regions
    I_ordered[q] = image[q]
    I_disordered[~q] = image[~q]
    
    # Plotting Original, Ordered and Disordered Image
    figure, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 2.5))
    img1 = ax1.imshow(image, cmap='gray', interpolation='nearest')
    ax1.set_title('Segmented image, before separation')
    plt.colorbar(img1, ax=ax1, shrink=0.5)
    
    img2 = ax2.imshow(I_ordered, cmap='gray', interpolation='nearest')
    ax2.set_title('Ordered region')
    plt.colorbar(img2, ax=ax2, shrink=0.5)

    img3 = ax3.imshow(I_disordered, cmap='gray', interpolation='nearest')
    ax3.set_title('Diordered region')
    plt.colorbar(img3, ax=ax3, shrink=0.5)

    plt.show()

        
    # Calculating order disorder ratio, percent coverage of ordered, disordered and overall
    order_disorder_ratio = np.sum(np.sum(I_ordered)) / np.sum(np.sum(I_disordered))
    
    percent_ordered =100 * (np.sum(np.sum(I_ordered)) / (image.shape[0] * image.shape[1]))
    
    percent_disordered =100 * (np.sum(np.sum(I_disordered)) / (image.shape[0] * image.shape[1]))
    
    percent_coverage = percent_ordered + percent_disordered

    print ('--- Disorderness of Image ---')    
    print ('Order-Disorder ratio = %.5f' %(order_disorder_ratio))
    print ('Order Percentage = %.5f' %(percent_ordered))
    print ('Disorder Percentage = %.5f' %(percent_disordered))
    print ('Coverage Percentage = %.5f' %(percent_coverage))
    
    return filt_img, I_ordered, I_disordered, order_disorder_ratio, percent_ordered, percent_disordered, percent_coverage 



