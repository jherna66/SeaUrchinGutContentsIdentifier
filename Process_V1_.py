# Title: Process_V1.py
# Author: Juliana Hernandez

from ij import IJ
from ij.plugin import Converter

# Get current image
imp = IJ.getImage()
imp2 = imp.duplicate()
IJ.run(imp2, "8-bit", "") # convert to 8-bit
IJ.run(imp2, "Auto Threshold", "method=Default white")
IJ.run(imp2, "Analyze Particles...", "size=4000-Infinity circularity=0-1.00 show=Masks include add in_situ") # "add" right after "include" to include roi to manager
imp2.close()
imp.show()