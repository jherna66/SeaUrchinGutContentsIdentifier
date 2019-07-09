# Title: Tag.py
# Author: Juliana Hernandez
# Description:

# Pyrhon Libraries

# Imagej Libraries
from ij import IJ
from ij.plugin.frame import RoiManager
from ij.plugin.filter import Analyzer
from ij.measure import ResultsTable
import ij.measure

# User Libraries

# Name: Tag
def tag(imp, roiMan, roiTotal, color):
	print "Inside of UrchinTag..."
	print "imp " + str(imp)
	# Set the color and line options for tagging
	IJ.run(imp, "Line Width...", "line=10")
	IJ.run("Colors...", "foreground=" + color + " background=black selection=magenta")

	if roiMan is not None:
		# Iterate through the ROIs
		for roi in xrange(roiTotal):
			# Select the ROI
			roiMan.select(roi)
			selectRoi = roiMan.getRoi(roi)
			
			# Tag the ROI
			IJ.run(imp, "Draw", "slice")
		# end for loop
		return 1
	else:
		return 0

def delete(imp, roiMan, roiTotal):

	# set results table
	rt = ResultsTable.getResultsTable()
	# set up analyzer
	analyzer = Analyzer(imp, 1, rt)
	totalPixels = 0
	# Set the color and line options for erasing
	IJ.run("Colors...", "foreground=black background=black selection=magenta")

	if roiMan is not None:
		# Iterate through the ROIs
		for roi in xrange(roiTotal):
			# Select the ROI
			roiMan.select(roi)
			selectRoi = roiMan.getRoi(roi)
			# measure
			analyzer.measure()
			meas = rt.getRowAsString(0)
			newLine = meas.split("	", 1)
			pixels = float(newLine[1])
			totalPixels = totalPixels + pixels
			# Tag the ROI
			IJ.run(imp, "Fill", "slice")
		# end for loop
		return totalPixels
	else:
		return 0

### Test the function ###
# Get image corresponding to the ROIs
#testImp = IJ.getImage()
# Open ROI manager
#rm = RoiManager.getInstance()
# Get number of objects found
#roiCount = rm.getCount()
# Test function
#print delete(testImp, rm, roiCount)
