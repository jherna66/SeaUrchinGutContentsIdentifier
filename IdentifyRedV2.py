# Title: IdentifyRed_V2.py
# Author: Juliana Hernandez
# Description: Identifies Red

print "Importing IdentifyRedV2.py..."

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.process import ImageProcessor, FloatProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager
#from ij.plugin.filter import Analyzer
#from ij.measure import ResultsTable
import ij.measure

# User Libraries
from UrchinLib import ProcessHSB

def identifyRed(imp):
	# Clear ROI manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()

	# set results table
#	rt = ResultsTable.getResultsTable()
	
	# Get hue from HSB stack
	impHue = ProcessHSB.getHue(imp)
	width = impHue.width
	height = impHue.height
	
	# Get processor for hue
	ipHue = impHue.getProcessor().convertToFloat()
	huePixels = ipHue.getPixels()

	# Bring brightness into the equation
	impBrightness = ProcessHSB.getBrightness(imp)
	IJ.run(impBrightness, "Auto Threshold", "method=MaxEntropy white")
	IJ.run(impBrightness, "Analyze Particles...", "size=10000-Infinity circularity=0.00-1.00 show=Masks in_situ")

	# Get processor for brightness
	ipBrightness = impBrightness.getProcessor().convertToFloat()
	brightnessPixels = ipBrightness.getPixels()

	# Do the thing now
	newPixels = map(ProcessHSB.redHueBackground, brightnessPixels, huePixels)
	
	# If hue < 30 and hue > 225, True
	#newNewPixels = map(ProcessHSB.redHue, newPixels)
	
	# Pause: Do this later
	ipNew = FloatProcessor(width, height, newPixels)
	impRed = ImagePlus("RedHue", ipNew)
	IJ.run(impRed, "8-bit", "") # convert to 8-bit
	#IJ.run(imp, "Options...", "iterations=20 count=1 black do=[Fill Holes]");
	impRed.show()
	
	# Logic AND pictures together
	#ic = ImageCalculator()
	#impRedMask = ic.run("AND create", impRed, impBrightness)
	#IJ.run(impRedMask, "8-bit", "") # convert to 8-bit
	#impRed.close()
	#impBrightness.close()
	#IJ.run(impRedMask, "Analyze Particles...", "size=90000-Infinity circularity=0-1.00 show=Masks add in_situ") # "add" right after "include" to include roi to manager

	#analyzer = Analyzer(imp, 1, rt)
	#analyzer.measure()
	#meas = rt.getRowAsString(0)
	#newLine = meas.split("	", 1)
	#red = float(newLine[1])
	
	#impRedMask.close()

	#return red
	

testImp = IJ.getImage()
result = identifyRed(testImp)
print "Done"
print type(result)
