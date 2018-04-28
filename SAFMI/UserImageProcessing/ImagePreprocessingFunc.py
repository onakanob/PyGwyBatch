# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 12:15:10 2018

@author: sarth
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage import morphology
import cv2



def savefile(filename, file):
    """ 
    Save an array to a txt file
    
    Args:
        filename: name of the txt file, a string
        file: data to be saved, 1D or 2D array-like
    
    Returns:
        txt file
        
    """

    output_file = np.savetxt(filename, file, fmt = '%.3f', delimiter = '\t')
    
    return output_file



def bckgrnd_correc_rect(image, row_len, col_len):
    """
    Background correction using a rectangular structuring element. 
    This function uses white_tophat from 
    skimage.morphology to return image minus 
    the morphological opening obtained from the structuring element.
    
    Args:
        image: image to be processed, a numpy array
        row_len: side-length of the rectangle filter, int
        col_len: side-length of the rectangle filter, int
    
    Returns:
        numpy array
    
    Raises:
        Errors when input type is wrong
    
    """
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # Checking the right data type for the row length of the rectangular structuring element
    assert type(row_len) == int, ('Wrong data type', 'row length must be a float')
    
    # Checking the right data type for the column length of the rectangular structuring element
    assert type(col_len) == int, ('Wrong data type', 'column length must be a float')
    
    # background corrrection 
    image_bckgrnd_corrected = morphology.white_tophat(image, morphology.rectangle(row_len,col_len))
    
    # plotting image
    plt.figure()
    plt.gray()
    plt.title('Background correction with rectangle')
    plt.imshow(image_bckgrnd_corrected)
    plt.colorbar()
    plt.show()
    
    return image_bckgrnd_corrected



def bckgrnd_correc_sq(image, length):
    """
    Background correction using a square structuring element. 
    This function uses white_tophat from 
    skimage.morphology to return image minus 
    the morphological opening obtained from the structuring element.    
    
    Args:
        image: image to be processed, a numpy array
        length: side-length of the square filter, int

    
    Returns:
        numpy array
    
    Raises:
        Errors when input type is wrong
    
    """
    
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # Checking the right data type for the length of the square structuring element
    assert type(length) == int, ('Wrong data type', 'length of the square structuring element must be a float')
    
    # background correction
    image_bckgrnd_corrected = morphology.white_tophat(image, morphology.square(length))
    
    # plotting image
    plt.figure()
    plt.gray()
    plt.title('Background correction with square')
    plt.imshow(image_bckgrnd_corrected)
    plt.colorbar()
    plt.show()
    
    return image_bckgrnd_corrected



def bckgrnd_correc_disk(image, radius):
    """
    Background correction using a disk structuring element. 
    This function uses white_tophat from 
    skimage.morphology to return image minus 
    the morphological opening obtained from the structuring element.    
    
    Args:
        image: image to be processed, a numpy array
        radius: radius of the disk filter, int

    
    Returns:
        numpy array
    
    Raises:
        Errors when input type is wrong
    
    """
    # Checking the right data type for the input image
    assert type(image) == np.ndarray, ('Wrong data type', 'image must be a numpy array')
    
    # Checking the right data type for the length of the square structuring element
    assert type(radius) == int, ('Wrong data type', 'radius of the disk structuring element must be a float')
    
    # background correction
    image_bckgrnd_corrected = morphology.white_tophat(image, morphology.disk(radius))
    
    # plotting image
    plt.figure()
    plt.gray()
    plt.title('Background correction with disk')
    plt.imshow(image_bckgrnd_corrected)
    plt.colorbar()
    plt.show()
    
    return image_bckgrnd_corrected
        

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
    
    # plotting the image
    plt.figure()
    plt.gray()
    plt.title('After background correction, gray-scale')
    plt.imshow(image_gray, cmap='gray')
    plt.colorbar()
    plt.show()
    
    return image_gray

        