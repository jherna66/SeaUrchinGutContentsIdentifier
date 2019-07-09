# Title: IdentifyStragglers.py
# Author: Juliana

# Turn this to test the function in this file
#test = True

# Python Libraries
import time
from array import zeros

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.plugin.frame import RoiManager
from ij.process import ImageProcessor, ColorProcessor
from ij.gui import GenericDialog
from ij.plugin.filter import Analyzer
from ij.measure import ResultsTable
import ij.measure

# User Libraries
from UrchinLib import Tag as UrchinTag
from UrchinLib import ProcessHSB

def learn(imp):

	IJ.run(imp, "Line Width...", "line=10")
	IJ.run("Colors...", "foreground=black background=black selection=red")
	
	# Clear ROI manager
	roiMan = RoiManager.getInstance()
	if roiMan is not None:
		roiMan.reset()

	# set results table
	rt = ResultsTable.getResultsTable()
	# set up analyzer
	analyzer = Analyzer(imp, 1, rt)
	
	impBrightness = ProcessHSB.getBrightness(imp)
	IJ.run(impBrightness, "8-bit", "")
	IJ.run(impBrightness, "Auto Threshold", "method=Shanbhag white")
	IJ.run(impBrightness, "Analyze Particles...", "size=50000-Infinity circularity=0.00-1.00 show=Masks add in_situ")
	
	# Pixel running total
	pixelTotal = zeros('f', 4)

	roiTotal = roiMan.getCount()
	
	if roiMan is not None:

		# Iterate throught the ROIs
		for roi in xrange(roiTotal):
			roiMan.select(roi)
			selectRoi = roiMan.getRoi(roi)
			
			option = getOptions()
			
			# measure
			analyzer.measure()
			meas = rt.getRowAsString(0)
			newLine = meas.split("	", 1)
			pixels = float(newLine[1])
			# Tag the ROI
			IJ.run(imp, "Fill", "slice")

			pixelTotal[0] = pixelTotal[0] + (option[0] * pixels)
			pixelTotal[1] = pixelTotal[1] + (option[1] * pixels)
			pixelTotal[2] = pixelTotal[2] + (option[2] * pixels)
			pixelTotal[3] = pixelTotal[3] + (option[3] * pixels)

		return pixelTotal
	else:
		return pixelTotal

def getOptions():  
	
	pixels = zeros('f', 4) # 4 elements

	# First Dialog Box
	item = ["coralline", "tunicate", "red", "macro", "background", "more than one"]
	gd = GenericDialog("Options")  
	gd.addRadioButtonGroup("options", item, 3, 2, "coralline")
	gd.showDialog()
	button = gd.getNextRadioButton()
	
	# Second Dialog Box
	gd2 = GenericDialog("Multiple Options")
	items = ["coralline", "tunicate", "red", "macro", "garbage"]
	defaultVal = [False] * 5
	gd2.addCheckboxGroup(2, 3, items, defaultVal)
	gd2.addNumericField("coralline %", 0, 0)
	gd2.addNumericField("tunicate %", 0, 0)
	gd2.addNumericField("red %", 0, 0)
	gd2.addNumericField("macro %", 0, 0)
	gd2.addNumericField("background %", 0, 0)
	
	if gd.wasCanceled():   
		return 0
	
	if button == "coralline":
		pixels[0] = 1
	elif button == "tunicate":
		pixels[1] = 1
	elif button == "red":
		pixels[2] = 1
	elif button == "macro":
		pixels[3] = 1
	elif button == "more than one":
		gd2.showDialog()
		checklist = gd2.getCheckboxes()
		pixels[0] = int(checklist[0].state) * (float(gd2.getNextNumber())/100)
		pixels[1] = int(checklist[1].state) * (float(gd2.getNextNumber())/100)
		pixels[2] = int(checklist[2].state) * (float(gd2.getNextNumber())/100)
		pixels[3] = int(checklist[3].state) * (float(gd2.getNextNumber())/100)
      	
	return pixels
	
### End functions ###

## Testing the function ##

#if test == True:
#	print "Testing"
	
	# Get image corresponding to the ROIs
#	testImp = IJ.getImage()
	# Test function
#	print learn(testImp)

#print getOptions()
