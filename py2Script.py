#This script called by py2Parse.py. It invokes a python 2 interpreter
#to call on each file recursively in a directory.

import sys
import os
import re

####### Customize Here #####
# Import the function to be called on each file #
from testFunction import testFunction \
    as myFunction          # Don't change this
###### End Customize #######

#Check local version info
if sys.version_info[0] != 2:
    print('This script requires a Python 2 interpreter')
    sys.exit(1)

#Parse command line arguments
directory = sys.argv[1]
file_spec = sys.argv[2]

#Walk the directory, printing the output from myFunction to stdout
for root, dirs, files in os.walk(directory): #gather a list of files in this directory
    for filename in files: #step through all files found
        file_path = os.path.join(root, filename) #get the full filepath
        if re.search(file_spec, file_path): #if file_spec appears as a substring in the file path
            sys.stdout.write(filename+"\t")
            sys.stdout.write(myFunction(file_path)+"\n")
