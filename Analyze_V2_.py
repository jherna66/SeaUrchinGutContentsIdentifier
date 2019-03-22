# Title: Analyze V1
# Author: Juliana

# Turn this to test the function in this file
test = True

# Libraries
from ij import IJ, ImagePlus
from ij.plugin.frame import RoiManager
from ij.process import ImageProcessor, ColorProcessor
from ij.gui import GenericDialog
#from ij.io import ImageProcessor
import time
from java.awt import Color

### Begin functions ###

def learn(imp, roiMan, roiTotal):
	IJ.run(imp, "Line Width...", "line=10")
	#ip.setColor(Color.magenta)
	if roiMan is not None:

		# Iterate throught the ROIs
		for roi in xrange(roiTotal):
			roiMan.select(roi)
			selectRoi = roiMan.getRoi(roi)
			tempImp = imp.duplicate()
			tempImp.show()
			#time.sleep(0.25)
			
			option = getOptions()
			# Check if canceled
			if option is 0:
				print "Canceled!!"
				tempImp.close()
				return 0
			# review options
			if option == "coraline":
				print option
			elif option == "turnicate":
				print option
			elif option == "macro":
				print option
			elif option == "red":
				print option
			elif option == "more than one":
				print option
			
			#ip.draw(selectRoi)
			tempImp.close()
		return 1
	else:
		return 0

def getOptions():  
	item = ["coraline", "tunicate", "macro", "red", "more than one", "background"]
	gd = GenericDialog("Options")  
	gd.addRadioButtonGroup("options", item, 3, 2, "coraline")
	gd.showDialog()  
	#  
	if gd.wasCanceled():   
		return 0
	button = gd.getNextRadioButton()
	if button == "more than one":
		gd2 = GenericDialog("Multiple Options")
		items = ["coraline", "tunicate", "macro", "red"]
		defaultVal = [False] * 4
		gd2.addCheckboxGroup(2, 2, items, defaultVal)
		gd2.showDialog()
	return button
	
### End functions ###

## Testing the function ##

if test == True:
	print "Testing"
	# Get image corresponding to the ROIs
	testImp = IJ.getImage()
	# Open Roi Manager
	rm = RoiManager.getInstance()
	# Get number of objects found
	roiCount = rm.getCount()
	# Test funxtion
	print learn(testImp, rm, roiCount)
