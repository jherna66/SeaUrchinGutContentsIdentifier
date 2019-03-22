# Title: FileFunctions.py

import os.path
import csv

# Name: initializeCSV
# Inputs: timeStr - string containing time and date to name CSV file
#		  fdest - destination directory of file
def initializeCSV(timeStr, fdest):
	print "Hi"
	# Check to see if destination directory exists
#	if os.path.exist(dstDir):
#		print "is path"
#		# create new path to create/open csv file
#		newPath = fDest + "\\" + timeStr + ".csv"
#		doc = os.path.basename(newPath) # might not be necessary
#		print doc
#		# check to see if file exists already
#		if os.path.isfile(newPath):
#			# If it does, do nothing
#			print "nothing"
#		else:
#			# create CSV file
#			print "nothing"
#		
#	else:
#		print "Destination directorty do not exists"