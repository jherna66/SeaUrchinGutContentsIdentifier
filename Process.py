# Title: Process.py
# Author: Juliana Hernandez
# Description: STEP 1 of the process

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.process import ImageProcessor, FloatProcessor
from ij.plugin import ImageCalculator
from ij.plugin.frame import RoiManager
from ij.plugin.filter import Analyzer
from ij.measure import ResultsTable
import ij.measure

# User Libraries
from UrchinLib import FileFunctions as UrchinFF
from UrchinLib import ProcessHSB
from UrchinLib import Tag as UrchinTag
from UrchinLib import IdentifyCoralline as UrchinCoral
from UrchinLib import IdentifyTunicate as UrchinTunicate
from UrchinLib import IdentifyRed as UrchinRed
from UrchinLib import IdentifyMacro as UrchinMacro


def process(imp):
	IJ.log("Processing " + str(imp.title) + "...")
	#impOut = imp.duplicate()
	impOut = imp
	impOut.show()
	
	# Prepare Roi Manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()

	### STEP 1 (Coralline, Tunicate) ###
	
	# Coralline
	UrchinCoral.identifyCoralline(impOut)
	roiCount = rm.getCount()
	coralline = UrchinTag.delete(impOut, rm, roiCount)
	IJ.log("Coralline: " + str(coralline))
	
	# Tunicate
	UrchinTunicate.identifyTunicate(impOut)
	roiCount = rm.getCount()
	tunicate = UrchinTag.delete(impOut, rm, roiCount)
	IJ.log("Tunicate: " + str(tunicate))
	
	
	### STEP 2 (Red, Macro) ###

	# Red
	UrchinRed.identifyRed(impOut)
	roiCount = rm.getCount()
	red = UrchinTag.delete(impOut, rm, roiCount)
	IJ.log("Red: " + str(red))
	
	# Macro
	UrchinMacro.identifyMacro(impOut)
	roiCount = rm.getCount()
	macro = UrchinTag.delete(impOut, rm, roiCount)
	IJ.log("Macro: " + str(macro))
	

	impOut.changes = False
	impOut.close()

	# Format String for output
	return UrchinFF.formatData(coralline, tunicate, red, macro)
	