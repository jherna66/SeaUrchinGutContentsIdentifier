# Title: Main_.py
# Author: Juliana Hernandez
# Description: Main script of UrchinPy

### Imagej Ops ###
#@ File   (label = "Input directory", style = "directory") srcFile
#@ String  (label = "File extension", value=".JPG") ext
#@ File   (label = "Output directory", style = "directory") dstFile

# Python Libraries
import os
import time

# Imagej Libraries
from ij import IJ
from ij import ImagePlus
from ij.plugin.filter import Analyzer
import ij.measure
from ij.measure import ResultsTable
from ij.plugin.frame import RoiManager
from ij.gui.PointRoi import promptBeforeDeleting

# User Libraries
from UrchinLib import FileFunctions as UrchinFF
from UrchinLib import Process as UrchinProcess


def main():

	# Get source and destination paths
	srcDir = srcFile.getAbsolutePath()
	dstDir = dstFile.getAbsolutePath()
	# Check to see source and destination paths exist
	if os.path.exists(srcDir) and os.path.exists(dstDir):

		# Get date and time for CSV naming
		localtime = time.localtime(time.time())
		timef = "{0:4d}{1:02d}{2:02d}_{3:02d}{4:02d}{5:02d}".format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec)
		# Reshape for inside of CSV file
		date = "{0:4d}-{1:02d}-{2:02d}".format(localtime.tm_year, localtime.tm_mon, localtime.tm_mday)
		
		# initialize the CSV
		pathCSV = UrchinFF.initializeCSV(timef, dstDir)

		# Open roi Manager
		rm = RoiManager.getRoiManager()
		IJ.log("RoiManger opened...")
		
		# walk through the source directory
		for root, directories, filenames in os.walk(srcDir):
			filenames.sort();
			for filename in filenames:
				filenameDown = filename.lower()
				extDown = ext.lower()
				if filenameDown.endswith(extDown):
					# Open image
					tempPath = os.path.join(srcDir, filename)
					imp = IJ.openImage(tempPath)
					results = UrchinProcess.process(imp)
					IJ.log("Results: " + str(results))
					
					imp.close()
					### Save data ###
					UrchinFF.appendNewRow(pathCSV, filename, date, results)
				
	else:
		IJ.log("Source or destination directorty do not exists")

	IJ.log("UrchinPy is done!")
	
main()
