#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:12:49 2018

@author: demiliu
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage import segmentation
import cv2
from ImageSegmentationFunc import seg_random_walker

def seg(bckgrnd_corr_image):
    """
    Wrapper function to perform and optimize segmentation of the image
    
    Args:
        bckgrnd_corr_image: image to be processed, numpy array
    
    Returns:
        numpy array
    
    """
    
    seg_ok = 'N'
    while seg_ok == 'N':
        print ('Please choose a threshold for segmentation from 0.0 to 1.0')
        default_threshold = input('Default dimensions? Y/N ')
        
        assert default_threshold == 'Y' or 'N', ('Answer to "default threshold?" can only be Y or N.')            
            
        if default_threshold == 'Y':            
            threshold = 0.15
            image_segmentation = seg_random_walker(bckgrnd_corr_image, threshold)
    
        elif default_threshold == 'N':
            threshold = float(input('Threshold (0.0 to 1.0): '))        
            image_segmentation = seg_random_walker(bckgrnd_corr_image, threshold)

            
        seg_ok = input('Are you okay with the segmentation? Y/N ')
    
    return image_segmentation
