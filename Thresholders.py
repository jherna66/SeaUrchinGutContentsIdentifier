# Title: Thresholders.py
# Authors: Juliana Hernandez
# Description: Custon thresholders

print "Importing Thresholders.py..."

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus
from ij.process import FloatProcessor

# User Libraries

def whiteThreshold(imp):
	width = imp.width
	height = imp.height
	ip = imp.getProcessor().convertToFloat()
	pixels = ip.getPixels()
	newPixels = map(white, pixels)
	ipNew = FloatProcessor(width, height, newPixels)
	impNew = ImagePlus("White", ipNew)
	IJ.run(impNew, "8-bit", "")
	return impNew

def white(w):
	if w >=180: #w >=190
		return 255
	else:
		return 0

### Test Functions ###

#imp = IJ.getImage()
#imp2 = whiteThreshold(imp)
#imp2.show()
