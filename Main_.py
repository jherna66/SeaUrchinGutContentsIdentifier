# TItle: Main_.py
# Author: Juliana Hernandez
# Description: Main script of UrchinPy

### Imagej Ops ###
#@ String (visibility=MESSAGE, value="Please enter image file location") msg1
#@ File   (label = "Input directory", style = "directory") srcFile
#@ String (visibility=MESSAGE, value="Please enter CVS file destination") msg2
#@ File   (label = "Output directory", style = "directory") dstFile

import time
import os.path
import csv

# Libraries
from Urchin import FileFunctions

def main():
	# Get source and destination paths
	srcDir = srcFile.getAbsolutePath()
	dstDir = dstFile.getAbsolutePath()

	# Get date and time for CSV naming
	localtime = time.localtime(time.time())
	timef = str(localtime.tm_mday) + str(localtime.tm_mon) + str(localtime.tm_year) + "_" + str(localtime.tm_hour) + str(localtime.tm_min) + str(localtime.tm_sec)

	initializeCSV(timef, dstFile)
	
	print timef
	
main()
