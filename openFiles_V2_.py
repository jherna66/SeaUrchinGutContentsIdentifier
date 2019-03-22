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
	datef =  str(localtime.tm_year) + str(localtime.tm_mday) + str(localtime.tm_mon)
	timef = datef + "_" + str(localtime.tm_hour) + str(localtime.tm_min) + str(localtime.tm_sec)
	
	# create new path
	newPath = dstDir + "\\" + timef + ".csv"

	#add is directory check
	if os.path.exists(srcDir) and os.path.exists(dstDir):
		# in itialize file that will contain all the information
		initializeCSV(newPath)
		# Iterate through the folder
		print srcDir
		for root, directories, filenames in os.walk(srcDir):
			filenames.sort()
			for filename in filenames:
				appendNewRow(newPath, filename, datef, 0, 0, 0, 0, 0,)
	else:
		print "Source or destination directorty do not exists"

# initialize CSV file
def initializeCSV(fname):

	doc = os.path.basename(fname)
	#print doc

	if os.path.isfile(fname):
		print "True"
	else:
		print "False"
		# create CSV file
		with open(fname, 'wb') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',') # , quotechar='', quoting = csv.QUOTE_MINIMAL
			filewriter.writerow(['Filename', 'Site', 'Date Taken', 'Sample#', 'Date Processed', 'Total Pixel Num', 'Coraline Pixel Num', 'Turnicate Pixel Num', 'Red Pixel Num', 'Green Pixel'])

# insert new line
# is currently overwriting rows
def appendNewRow(cname ,fname, currentTime, totalPix, corralinePix, turnicatePix, redPix, greenPix):
	# get file name information
	doc = os.path.basename(fname)
	temp = doc.split('.', 2)
	name = str(temp[0]) + '.' + str(temp[1])
	info = name.split('_') # list of tokenized title
	site = info[0]
	dateCollected = info[1]
	sampleNum = info[2]
	print "im here"
	with open(cname, 'ab') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting = csv.QUOTE_MINIMAL) # 
		filewriter.writerow([str(name[0]) + ',' + str(site) + ',' + str(dateCollected) + ',' + str(sampleNum) + ',' + str(currentTime) + ',' + str(totalPix) + ',' + str(corralinePix) + ',' + str(turnicatePix) + ',' + str(redPix) + ',' + str(greenPix)])
		print str(name[0]) + ',' + str(site) + ',' + str(dateCollected) + ',' + str(sampleNum) + ',' + str(currentTime) + ',' + str(totalPix) + ',' + str(corralinePix) + ',' + str(turnicatePix) + ',' + str(redPix) + ',' + str(greenPix)


main()