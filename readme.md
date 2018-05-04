PyGwy Batch File Handler

Minimal framework to apply a PyGwy function (or any other function with a Python 2 dependency) to multiple files in a directory. This framework will work when executed from a Python 3 environment as long as you can provide a path to a python 2 interpreter. See 'Gwyddion Packages.zip' for PyGwy's dependencies - extract these to the python 2 install directory. 


runPython2Func.py: 
Start here - modify variables at the top to specify a python 2 interpreter, specify the starting point for the file search, and specify a regex expression for identifying which files to parse. Execute this script to run the whole workflow.

At the end, use the array output_data to parse results, or pipe the output of this file to a .txt or .csv file for external post-processing


py2Script.py: 
Modify line 13 to import a function that will be called for each file. The function should take exactly one input, which is a full filepath. It should output a single string.


testFunction.py: 
An example of a function that imports the gwyddion PyGwy library and calls some function(s) on a file, returning a single string.
