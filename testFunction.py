import sys
sys.path.insert(0, 'C:\Program Files (x86)\Gwyddion\\bin')
import gwy

# This function should return a string. For multiple values, delineate using \t
def testFunction(filename):
    with open(filename) as f:
        I = gwy.DataField(8,8,1.0,1.0)
        return filename
        f.close()
