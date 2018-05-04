#Usage: py2Script directory file_spec

import sys
import os
import re

if sys.version_info[0] != 2:
    print('This script requires a Python 2 interpreter')
    sys.exit(1)

directory = sys.argv[1]
file_spec = sys.argv[2]

def testFunction(filename):
    with open(filename) as f:
        return filename
        f.close()

for root, dirs, files in os.walk(directory):
    for filename in files:
        file_path = os.path.join(root, filename)
        if re.search(file_spec, file_path):
            sys.stdout.write(filename+"\t")
            sys.stdout.write(testFunction(file_path)+"\n")

#inputFile = sys.argv[1]
#print(testFunction(inputFile))

