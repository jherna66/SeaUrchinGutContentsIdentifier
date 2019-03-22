# Title: Process_V1.py
# Author: Juliana Hernandez

# Administrative stuff
import inspect, os
thisFile = "C:\\Users\\Juliana\\Documents\\Fiji.app\\scripts\\UrchinPy\\"
print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory
import sys
sys.path.append(thisFile)

# Libraries
from ij import IJ
from ij.plugin import Converter, ImageCalculator
from ij.plugin.frame import RoiManager

# User libraries
#from Analyze_V1 import learn

# Open Roi Manager
rm = RoiManager.getInstance()
if rm is not None:
	rm.reset()

# Get current image
imp = IJ.getImage()
imp2 = imp.duplicate()
IJ.run(imp2, "8-bit", "") # convert to 8-bit
IJ.run(imp2, "Auto Threshold", "method=Shanbhag white")
IJ.run(imp2, "Analyze Particles...", "size=10000-Infinity circularity=0-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager

# Remove background
ic = ImageCalculator()
imp3 = ic.run("AND create", imp, imp2)
imp.close()
imp2.close()
imp3.show()

### Begin manipulating ROIs ###

rm = RoiManager.getInstance()
# Get number of objects found
roiCount = rm.getCount() 
print "Number of Particles found:" + str(roiCount)
# Count is from 0 to (roiCount - 1)

# analyzing a single particle
#learn(imp3, rm, roiCount)
