#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 08:56:28 2018

@author: demiliu
"""

import numpy as np
import matplotlib.pyplot as plt
from ImagePreprocessingFunc import convert_to_grayscale

import ImageSegmentation as isg
import ImageSeparation as isp
import ImagePreprocessing as ip



def loadimage(filename):
    """load the user file, .txt format"""    
    txtfile = np.loadtxt(filename, delimiter = '\t')
    
    return txtfile


def savefile(filename, file):
    """saves file"""
    output_file = np.savetxt(filename, file, fmt = '%.3f', delimiter = '\t')
    
    return output_file
    

def savecalculation(filename, file):
    """ saves calculation of disorder-ness:
        1st number: order-disorder ratio
        2nd number: percent ordered
        3rd number: percent disordered
        4th number: percent coverage"""
    output = np.empty((4, 1))
    output[0, 0] = file[0]
    output[1, 0] = file[1]
    output[2, 0] = file[2]
    output[3, 0] = file[3]
    
    output_file = np.savetxt(filename, output, fmt = '%.3f', delimiter = '\t')

    return output_file



#runs one_k() and multiple_k() from command line
if __name__ == '__main__':
    """main function to run functions based on user interaction"""
    
    print ('---AFM Image Segregation---')
    print ('Hello! Welcome to AFM Image Separation!')
    print ('Please enter the filename WITHOUT .txt')
    
    user_filename = input('Filename: ')
    image = loadimage(user_filename + '.txt')


    #display unprocessed image
    plt.figure()
    plt.title('Raw image')
    plt.imshow(image, cmap='gray')
    plt.colorbar()
    plt.show()


    #Perform image processing based on user's need
    print ('How would you like to process the image?')    
    processing_need = input('Please choose from: Background Removal, Segmentation, Separation. ')
    

    if processing_need == 'Background Removal':
        #remove background and save corrected image
        bckgrnd_corr_image = ip.bckgrnd_corr(image)
        bkgnd_savefile = savefile(user_filename + '_bkgn_corr.txt', bckgrnd_corr_image)
        
        #convert image to gray-scale and save gray-scale image
        grayscale_image = convert_to_grayscale(bckgrnd_corr_image)        
        grayscale_savefile = savefile(user_filename + '_bkgn_corr_grayscale.txt', grayscale_image)
        print ('Thanks for using AFM Image Separation. Have a nice day!') 
    
    elif processing_need == 'Segmentation':
        #remove background and save corrected image
        bckgrnd_corr_image = ip.bckgrnd_corr(image)
        bkgnd_savefile = savefile(user_filename + '_bkgn_corr.txt', bckgrnd_corr_image)
        
        #convert image to gray-scale and save gray-scale image
        grayscale_image = convert_to_grayscale(bckgrnd_corr_image)        
        grayscale_savefile = savefile(user_filename + '_bkgn_corr_grayscale.txt', grayscale_image)
        
        #segment image
        segmented_image = isg.seg(grayscale_image)
        segmented_savefile = savefile(user_filename + '_segmented.txt', grayscale_image)
        print ('Thanks for using AFM Image Separation. Have a nice day!') 
    
    
    elif processing_need == 'Separation':
        #remove background and save corrected image
        bckgrnd_corr_image = ip.bckgrnd_corr(image)
        bkgnd_savefile = savefile(user_filename + '_bkgn_corr.txt', bckgrnd_corr_image)
        
        #convert image to gray-scale and save gray-scale image
        grayscale_image = convert_to_grayscale(bckgrnd_corr_image)        
        grayscale_savefile = savefile(user_filename + '_bkgn_corr_grayscale.txt', grayscale_image)
        
        #segment image
        segmented_image = isg.seg(grayscale_image)
        segmented_savefile = savefile(user_filename + '_segmented.txt', segmented_image)

        #separate images
        separated_image = isp.sep(segmented_image)
        filtered_savefile = savefile(user_filename + '_filtered.txt', separated_image[0])
        ordered_savefile = savefile(user_filename + '_ordered.txt', separated_image[1])
        disordered_savefile = savefile(user_filename + '_disordered.txt', separated_image[2])
        calculation_savefile = savecalculation(user_filename + '_disorder_calculation.txt', separated_image[3:])
        print ('Thanks for using AFM Image Separation. Have a nice day!') 
        
    else:
        print ("Sorry! We can't help you...")
        
        exit
