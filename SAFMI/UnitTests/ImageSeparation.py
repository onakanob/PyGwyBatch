#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:11:44 2018

@author: demiliu
"""
from ImageSeparationFunc import order_disorder_separation


def sep(segmented_image):
    """
    Wrapper function to perform and optimize segmentation of the image.
    
    Args:
        segmented_image: image to be separated by disorder level,
        numpy array
        
    Returns:
        output from order_disorder_separation
    
    """
    
    #Optimize separation results based on user interaction
    #After each run of the separation function, the user will be asked
    #if separation results look okay. The function will run 
    #until user is okay with the separation.

    sep_ok = 'N'
    while sep_ok == 'N':
        
        #ask user the parameters of the filter
        #if the user chooses to not to use the default setting,
        #the program will ask user to enter parameters
        print ('Please enter the parameters for image separation')
        default_parameter = input('Default parameters? Y/N ')
        
        assert default_parameter == str('Y') or ('N'), ('Answer to "default parameters?" can only be Y or N.')            
        
        if default_parameter == 'Y':            
            percentile = 30
            size = 10
            image_separation = order_disorder_separation(segmented_image, percentile, size)
            sep_ok = input('Are you okay with the separation? Y/N ')

        elif default_parameter == 'N':
            percentile = int(input('Percentile (0 to 100): '))
            size = int(input('Size (integer): '))        
            image_separation = order_disorder_separation(segmented_image, percentile, size)
            sep_ok = input('Are you okay with the separation? Y/N ')
        
        else:
            print ('Please enter Y or N only for "Default parameters?".')
            sep_ok = 'N'

    
    return image_separation