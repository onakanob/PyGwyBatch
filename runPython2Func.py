# runPython2Func: invokes a subprocess cmd to execute a python 2 script and retrieve the output

#To capture the results of this process, recommended to pipe to a
#text or csv file:
#runPython2Func.py > myResults.txt

import sys
import subprocess
import re
import numpy as np

####### Customize Here #######
python_2_command = 'py -2'   #command or path to the Python 2.X interpreter
directory = '.\data'         #directory containing files to be processed
regex = '.txt'               #regular expression to use to recognize files
num_outputs = 1              #how many outputs are generated by your function?
###### End Customize #########

script_path = '.\py2Script.py' #path to py2Script.py

#Assemble a terminal command sequence to call the python 2 script and pass
#it to the system subprocess
command = python_2_command + ' ' + script_path + ' ' + directory + ' ' + regex
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate() #Capture subprocess stdout bitstring

output_string = output.decode('utf-8') #Output as text table

# Copy of output as numpy array, if further analysis is needed
output_data = np.array(re.split('\r\n|\t', output_string))
output_data = output_data[:-1].reshape(-1,1+num_outputs) #This step is touchy, comment out if it's causing problems

# Print output to stdout - good for a quick look, or pipe to a text or csv file for postprocessing
print(output_string)
