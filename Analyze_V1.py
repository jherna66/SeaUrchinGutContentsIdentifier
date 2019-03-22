# Title: Analyze V1
# Author: Juliana

# Turn this to test the function in this file
test = True

# Libraries
from ij import IJ
from ij.plugin.frame import RoiManager
import time

### Begin functions ###

def learn(imp, roiMan, roiTotal):
	# Who am I?
	IJ.setBackgroundColor(0, 0, 0)
	
	if roiMan is not None:
		# Iterate throught the ROIs
		for roi in xrange(roiTotal):
			roiMan.select(roi)
			tempImp = imp.duplicate()
			
			tempImp.show()
			time.sleep(0.5)
			tempImp.close()
		return 1
	else:
		return 0

	
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
