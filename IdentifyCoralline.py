# Title: IdentifyCoralline.py
# Author: Juliana Hernandez
# Description: Counts the pixels total pixels in the image

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
from UrchinLib import Thresholders as TH

def identifyCoralline(imp):
	# Prepare Roi Manager
	rm = RoiManager.getInstance()
	if rm is not None:
		rm.reset()

	# set results table
	rt = ResultsTable.getResultsTable()

	impTemp = imp.duplicate()
	IJ.run(impTemp, "8-bit", "") # convert to 8-bit
	impCoralline = TH.whiteThreshold(impTemp)
	impTemp.close()

	IJ.run(impCoralline, "Analyze Particles...", "size=10000-Infinity circularity=0-0.50 show=Masks add in_situ")
	analyzer = Analyzer(imp, 1, rt)
	analyzer.measure()
	meas = rt.getRowAsString(0)
	newLine = meas.split("	", 1)
	coralline = float(newLine[1])
	return coralline