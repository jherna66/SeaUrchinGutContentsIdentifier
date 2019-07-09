# Title: Untitled
# Author: Juliana Hernandez
# Description: None

print "Imported Untitled.py..."

# Python Libraries

# Imagej Libraries
from ij import IJ
from ij.plugin.frame import RoiManager

# User Libraries

def process(imp):
	# Open and clear Roi Manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()

	# Duplicate image
	imp2 = imp.duplicate()
	
	#IJ.run(imp2, "8-bit", "") # convert to 8-bit
	IJ.run(imp2, "HSB Stack", "")
	IJ.run(imp2, "Delete Slice", "")
	IJ.run(imp2, "Delete Slice", "")
	IJ.run(imp2, "Auto Threshold", "method=MaxEntropy white") #Shanbhag #MaxEntropy
	IJ.run(imp2, "Analyze Particles...", "size=10000-Infinity circularity=0-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager
	imp2.show()
	
	return 0	

tempImp = IJ.getImage()
process(tempImp)