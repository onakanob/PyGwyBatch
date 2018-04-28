import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from skimage import morphology, color, segmentation, feature, filters, io
import cv2


from ImageSegmentationFunc import convert_to_grayscale
from ImageSegmentation import seg
from ImagePreprocessing import bckgrnd_correc_rect

from unittest import mock
from unittest import TestCase

I1_test = np.loadtxt('tdj_grbp5_1um_1hr_3rd_020717.001.txt')
gh = bckgrnd_correc_rect(I1_test,10,200)
plt.close()
gray_I1 = convert_to_grayscale(gh)
plt.close()

class segTests(TestCase):
    @mock.patch('ImageSegmentation.input', create=True)

    #check expected outputs for specific user inputs 
    def test_seg(self, mocked_input):
        mocked_input.side_effect = ['Y', 'Y']
        resulty = seg(gray_I1)
        plt.close()
        py = type(resulty)
        self.assertEqual(py, np.ndarray)
    
 
