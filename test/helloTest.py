#!usr/env/bin python
#Test Script, just to validate the dir structure

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pyGwyBatch.functions import hello

hello()
