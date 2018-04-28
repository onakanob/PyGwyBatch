from __future__ import absolute_import, division, print_function
from os.path import join as pjoin

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
# _version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: MIT License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

# Description should be a one-liner:
description = "SAFMI: Segmentation of AFM Image data and prediction of properties"
# Long description will go up on the pypi page
long_description = """
Shablona
========
SAFMI is a software for the identification of different textural components and their segmentation in AFM images of self assembled peptide structures. From a .txt file image data of the system from AFM, the software helps front-end users approximate the effect of 
natural tip drift which is ubiquitous in AFM characterization, cancel noise, detect different textures based on how ordered or disordered the self-assembly is and calculate the percent coverage of each texture, overall percent coverage of the self assembled 
peptides, and the ordered to disordered ratio as a means of characterizing the results in terms of degree of disorderedness. This will help evaluate the self assembly properties of the peptides on the substrates for the processing conditions. A second use case of 
SAFMI is to output the same data even without the availability of an AFM image, if the processing parameters such as pH and peptide-concentration are known. A k-Nearest Neighbors classification algorithm is used for a regression analysis of the image parameters 
(percent coverage, Ratio of Ordered to Disordered, degree of disorderedness) from 55 512x512 pixel size AFM images of such systems, 75% of which are used for training and 25% for validation. This technique predicts the estimated Ratio of Ordered to Disordered for 
an absent image if the processing conditions are known
To get started using these components in your own software, please go to the
repository README_.
.. _README: https://github.com/liud16/direct18project/blob/master/README.md
License
=======
``SAFMI`` is licensed under the terms of the MIT license. See the file
"LICENSE" for information on the history of this software, terms & conditions
for usage, and a DISCLAIMER OF ALL WARRANTIES.
"""

NAME = "SAFMI_AFM"
MAINTAINER = "demi_sarthak_chris_sid"
MAINTAINER_EMAIL = "rathsidd@uw.edu"
DESCRIPTION = description
LONG_DESCRIPTION = long_description
URL = "http://github.com/liud16/direct18project"
DOWNLOAD_URL = ""
LICENSE = "MIT"
AUTHOR = "SID_SARTHAK_DEMI_CHRIS"
AUTHOR_EMAIL = "rathsidd@uw.edu"
PLATFORMS = "OS Independent"
MAJOR = _version_major
MINOR = _version_minor
MICRO = _version_micro
VERSION = __version__
PACKAGE_DATA = {'SAFMI': [pjoin('data', '*')]}
REQUIRES = ["numpy","scipy","scikit-learn","scikit-image","openCV","pandas","matplotlib"]
