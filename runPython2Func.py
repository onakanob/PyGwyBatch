# py2Parse: invokes a subprocess cmd to execute a python 2 script and retrieve the output
import sys
import subprocess
import re
import numpy as np

####### Customize Here #######
python_2_command = 'py -2'   #command or path to the Python 2.X interpreter
script_path = 'py2Script.py' #path to py2Script.py
directory = '.\data'         #directory containing files to be processed
regex = '.txt'               #regular expression to use to recognize files
###### End Customize #########

command = python_2_command + ' ' + script_path + ' ' + directory + ' ' + regex
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

output_string = output.decode('utf-8') #Output as text table

# Output as numpy array, if further analysis is needed
output_data = np.array(re.split('\r\n|\t', output_string))
output_data = output_data[:-1].reshape(-1,2)

# Print output to stdout - good for quick view, or pipe to a text or csv file for postprocessing
print(output_string)
