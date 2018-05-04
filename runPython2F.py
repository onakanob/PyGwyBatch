# py2Parse: invokes a subprocess cmd to execute a python 2 script and retrieve the output
import sys
import subprocess

####### Customize Here #######
python_2_command = 'py -2'   #command or path to the Python 2.X interpreter
script_path = 'py2Script.py' #path to py2Script.py
directory = '.\data'         #directory containing files to be processed
regex = '.txt'               #regular expression to use to recognize files
###### End Customize #########

command = python_2_command + ' ' + script_path + ' ' + directory + ' ' + regex
process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output.decode("utf-8"))
