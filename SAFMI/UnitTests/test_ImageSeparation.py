import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from skimage import morphology, color, segmentation, feature, filters, io
from sklearn import cluster
from scipy import ndimage
import cv2



from ImageSeparation import sep
from ImageSegmentationFunc import convert_to_grayscale
from ImageSegmentationFunc import seg_random_walker
from ImagePreprocessing import bckgrnd_correc_rect

from unittest import mock
from unittest import TestCase
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


class sepTests(TestCase):
    @mock.patch('ImageSeparation.input', create=True)

    #check expected outputs for specific user inputs 
    def test_sep(self, mocked_input):
        mocked_input.side_effect = ['Y','Y']
        result_sep = sep(trial_t)
        p_sep = type(result_sep)
        self.assertEqual(p_sep, tuple)
