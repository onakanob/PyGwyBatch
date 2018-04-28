# -*- coding: utf-8 -*-
"""
Created on Wed Mar 07 12:20:10 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import segmentation
import cv2


def convert_to_grayscale(image):
    """
    Converting the image to grayscale - 
    where minimum pixel value is 0.0 and maximum pixel value is 1.0
    
    Args:
        image: image to be processed, numpy array
    
    Returns:
        numpy array
    
    Raises:
        Errors when input type is wrong
        
    """
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # converting to grayscale
    dst = np.zeros(image.shape)
    image_gray = cv2.normalize(image, dst, 0.0, 1.0, cv2.NORM_MINMAX)
    

    
    return image_gray


def seg_random_walker(image, marker_threshold):
    
    """
    Segment image into two regions using skimage random walker 
    segmentation algorithm. Input image must be gray-scale. 
    This function will provide segmented image and marker positions
    as the output.
    
    Args:
        image: image to be processed, numpy array
        marker_threshold: threshold for segmentation, float
    
    Returns:
        numpy array
    
    Raises:
        Errors when input type is wrong
        Error when marker_threshold is out of the range of 0 and 1
    
    """
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong image data type', 'image must be a numpy array')
    
    # Checking that the input image is grayscale and not RGB or something else
    assert np.max(image) == 1.0 or 1, ('Wrong input image type', 'image must be grayscale')
    
    assert np.min(image) == 0.0 or 0, ('Wrong input image type', 'image must be grayscale')
    
    # Checking the right data type and range for marker threshold value
    #assert marker_threshold == float, ('Marker threshold must be a float number.')    
    assert 0.0 <= marker_threshold <= 1.0, ('Marker threshold out of range', 'Marker threshold must be between 0 and 1')    
    
    # Random walker segmentation    
    markers = np.zeros(image.shape)
    markers[image < marker_threshold] = 1 # ordered regions
    markers[image > marker_threshold] = 2 # disordered regions
    
    # Segment image based on order and disorder;
    # convert to gray-scale
    segmented = segmentation.random_walker(image, markers)
    seg_image = convert_to_grayscale(segmented)
    
    
    # Plotting the segemented, original image and markers  
    figure, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 2.5))
    img1 = ax1.imshow(image, cmap='gray', interpolation='nearest')
    ax1.set_title('Original Image')
    plt.colorbar(img1, ax=ax1, shrink=0.5)
    
    img2 = ax2.imshow(seg_image, cmap='gray', interpolation='nearest')
    ax2.set_title('Segmented Image')
    plt.colorbar(img2, ax=ax2, shrink=0.5)

    img3 = ax3.imshow(markers, cmap='gray', interpolation='nearest')
    ax3.set_title('Markers')
    plt.colorbar(img3, ax=ax3, shrink=0.5)

    plt.show()

       
    return seg_image
 




