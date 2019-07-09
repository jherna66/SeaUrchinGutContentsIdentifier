# Title: IdentifyRed.py
# Author: Juliana Hernandez
# Description: Identifies Red

print "Importing IdentifyRed.py..."

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.process import ImageProcessor, FloatProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager

# User Libraries
from UrchinLib import ProcessHSB

def identifyRed(imp):
	# Clear ROI manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()
	
	# Get hue from HSB stack
	impHue = ProcessHSB.getHue(imp)
	width = impHue.width
	height = impHue.height
	
	# Get processor for hue
	ipHue = impHue.getProcessor().convertToFloat()
	huePixels = ipHue.getPixels()

	# Bring brightness into the equation
	impBrightness = ProcessHSB.getBrightness(imp)
	IJ.run(impBrightness, "Auto Threshold", "method=Default white")
	#IJ.run(impBrightness, "Analyze Particles...", "size=10000-Infinity circularity=0.00-1.00 show=Masks in_situ")
	
	# If hue < 30 and hue > 225, True
	newPixels = map(ProcessHSB.redHue, huePixels)
	
	# Pause: Do this later
	ipNew = FloatProcessor(width, height, newPixels)
	impRed = ImagePlus("RedHue", ipNew)
	IJ.run(impRed, "8-bit", "") # convert to 8-bit
	
	# Logic AND pictures together
	ic = ImageCalculator()
	impRedMask = ic.run("AND create", impRed, impBrightness)
	IJ.run(impRedMask, "8-bit", "") # convert to 8-bit
	IJ.run(impRedMask, "Analyze Particles...", "size=10000-Infinity circularity=0.00-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager
	
	impHue.close()
	impBrightness.close()
	impRed.close()
	impRedMask.close()
	
### Testing ###
#testImp = IJ.getImage()
#result = identifyRed(testImp)
#print "Done"
#print type(result)
