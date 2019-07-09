# Title: Analysis.py
# Author: Juliana Hernandez
# Description: Main analysis function for UrchinPy

# Python Libraries

# Imagej Libraries
from ij import IJ
from ij.plugin import Converter, ImageCalculator
from ij.plugin.frame import RoiManager

# User Libraries


# Name: createMask
# Inputs: imp - image to be processed
# Output: impNew - imp without the background
def create(imp):
	# Prep Roi Manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()

	# Get current image
	imp2 = imp.duplicate()
	IJ.run(imp2, "8-bit", "") # convert to 8-bit
	IJ.run(imp2, "Auto Threshold", "method=Shanbhag white")
	IJ.run(imp2, "Analyze Particles...", "size=10000-Infinity circularity=0-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager
	
	# Remove background
	ic = ImageCalculator()
	imp3 = ic.run("AND create", imp, imp2)
	imp.close()
	imp2.close()
	
	### Begin manipulating ROIs ###
	
	rm = RoiManager.getInstance()
	# Get number of objects found
	roiCount = rm.getCount() 
	print "Number of Particles found:" + str(roiCount)
	# Count is from 0 to (roiCount - 1)

	# analyzing a single particle
#learn(imp3, rm, roiCount)
