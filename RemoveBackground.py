# Title: RemoveBackgroung.py

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.plugin import ImageCalculator

# User Libraries
from UrchinLib import ProcessHSB

imp = IJ.getImage()
impOut = imp.duplicate()
impOut.show()
# Get hue from HSB stack
impBrightness = ProcessHSB.getBrightness(imp)
IJ.run(impBrightness, "Auto Threshold", "method=Default white")

impBrightness.show()