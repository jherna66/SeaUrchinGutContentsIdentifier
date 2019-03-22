# Title: openFiles_.py
# Author: Juliana Hernandez
# Description: This script is meant to automatically open the images
# and write the resulting CVS file

#@ String (visibility=MESSAGE, value="Please enter file location") msg
#@ File   (label = "Input directory", style = "directory") srcFile
#@ File   (label = "Output directory", style = "directory") dstFile

import os
import os.path
from ij import IJ, ImagePlus
from ij.io import FileSaver
import csv
import pdb
import time

def main():
	# Begin by getting the source and destination paths
	srcDir = srcFile.getAbsolutePath()
	dstDir = dstFile.getAbsolutePath()

	localtime = time.localtime(time.time())
	timef = str(localtime.tm_mday) + str(localtime.tm_mon) + str(localtime.tm_year) + "_" + str(localtime.tm_hour) + str(localtime.tm_min) + str(localtime.tm_sec)

	# create new path
	newPath = dstDir + "\\" + timef + ".csv"
	print newPath
	
	if os.path.exists(srcDir) and os.path.exists(dstDir):
		# in itialize file that will contain all the information
		initializeCSV(newPath)
		# Iterate through the folder
		for root, directories, filenames in os.walk(srcDir):
			filenames.sort()
			print str(filenames) # convert to string to at new line
		#for x in range(0,len(filenames)):
		 	#print filenames[x]
	else:
		print "Source or destination directorty do not exists"

def initializeCSV(fname):

	doc = os.path.basename(fname)
	print doc

	if os.path.isfile(fname):
		print "True"
	else:
		print "False"
		# create CSV file
		with open(fname, 'wb') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting = csv.QUOTE_MINIMAL)
			filewriter.writerow(['Filename', 'Site', 'Date Taken', 'Sample#', 'Date Processed', 'Total Pixel Num', 'Coraline Pixel Num', 'Turnicate Pixel Num', 'Red Pixel Num', 'Green Pixel'])




main()