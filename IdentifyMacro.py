# Title: IdentifyMacro.py
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

def identifyMacro(imp):
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

	# Get macro hue
	newPixels = map(ProcessHSB.macroHue, huePixels)
	ipNew = FloatProcessor(width, height, newPixels)
	impMacro = ImagePlus("MacroHue", ipNew)
	
	# Bring brightness into the equation
	impBrightness = ProcessHSB.getBrightness(imp)
	IJ.run(impBrightness, "Auto Threshold", "method=Default white") #MaxEntropy
	#IJ.run(impBrightness, "Analyze Particles...", "size=10000-Infinity circularity=0.10-1.00 show=Masks in_situ") # "add" right after "include" to include roi to manager
	
	# Logic AND pictures together
	ic = ImageCalculator()
	impMacroMask = ic.run("AND create", impMacro, impBrightness)
	IJ.run(impMacroMask, "8-bit", "") # convert to 8-bit
	impMacro.close()
	impBrightness.close()
	IJ.run(impMacroMask, "Analyze Particles...", "size=10000-Infinity circularity=0-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager
		
	impMacroMask.close()
	#imp.show()
	#rm = RoiManager.getInstance()
	#return rm

#testImp = IJ.getImage()
#result = identifyRed(testImp)
#print type(result)