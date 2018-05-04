# py2Parse: invokes a subprocess cmd to execute a python 2 script and retrieve the output

import sys
import subprocess

if sys.version_info[0] != 3:
    print('This script requires a Python 3 interpreter... just call the python 2 script directly.')
    sys.exit(1)

def invokePy2(script_path, directory, regex):
    command = "py -2 " + script_path + " " + directory + " " + regex
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

output = invokePy2("py2Script.py", "..\data", ".txt")
print(output.decode("utf-8"))
