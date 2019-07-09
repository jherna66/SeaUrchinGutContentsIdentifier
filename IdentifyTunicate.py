# Title: IdentifyTunicate.py
# Author: Juliana Hernandez
# Description: Identifies Macro

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.process import ImageProcessor, FloatProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager

# User Libraries
from UrchinLib import ProcessHSB

def identifyTunicate(imp):
	# Clear ROI manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()
	
	# Get hue from HSB stack
	impHue = ProcessHSB.getHue(imp)
	width = impHue.width
	height = impHue.height
	
	# Get processor
	ipHue = impHue.getProcessor().convertToFloat()
	huePixels = ipHue.getPixels()

	# Get macro hue because it is the same color
	newPixels = map(ProcessHSB.macroHue, huePixels)
	ipNew = FloatProcessor(width, height, newPixels)
	impTunicate = ImagePlus("MacroHue", ipNew)
	
	# Bring brightness into the equation
	impBrightness = ProcessHSB.getBrightness(imp)
	IJ.run(impBrightness, "Auto Threshold", "method=MaxEntropy white")
	#IJ.run(impBrightness, "Analyze Particles...", "size=10000-Infinity circularity=0.10-1.00 show=Masks in_situ") # "add" right after "include" to include roi to manager
	
	# Logic AND pictures together
	ic = ImageCalculator()
	impTunicateMask = ic.run("AND create", impTunicate, impBrightness)
	IJ.run(impTunicateMask, "8-bit", "") # convert to 8-bit
	impTunicate.close()
	impBrightness.close()
	IJ.run(impTunicateMask, "Analyze Particles...", "size=10000-Infinity circularity=0.50-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager
		
	impTunicateMask.close()
	#imp.show()
	#rm = RoiManager.getInstance()
	#return rm

#testImp = IJ.getImage()
#result = identifyTunicate(testImp)
#print type(result)