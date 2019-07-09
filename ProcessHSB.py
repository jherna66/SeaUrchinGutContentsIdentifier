# Title: ProcessHSB.py
# Author: Juliana Hernandez
# Description: Script used to obtain Hue and Saturation images

print "Importing ProcessHSB.py..."

# Python Libraries

# Imagej Libraries
from ij import IJ, ImagePlus, ImageStack

# User Libraries

def getHue(imp):
	ip = imp.getProcessor()
	hsbStack = ip.getHSBStack() # idices: 1 - hue, 2 - saturation, 3 - brightness
	hp = hsbStack.getProcessor(1)
	imp2 = ImagePlus("Hue", hp)
	return imp2

def getSaturation(imp):
	ip = imp.getProcessor()
	hsbStack = ip.getHSBStack() # idices: 1 - hue, 2 - saturation, 3 - brightness
	sp = hsbStack.getProcessor(2)
	imp2 = ImagePlus("Saturation", sp)
	return imp2

def getBrightness(imp):
	ip = imp.getProcessor()
	hsbStack = ip.getHSBStack() # idices: 1 - hue, 2 - saturation, 3 - brightness
	bp = hsbStack.getProcessor(3)
	imp2 = ImagePlus("Brightness", bp)
	return imp2

def redHue(h):
	if h <= 25:	#h <= 30 or h >=225
		return 255
	else:
		return 0

def macroHue(h):
	if h >= 25 and h <=50:
		return 255
	else:
		return 0

def redHueBackground(b, h):
	if b == 0:
		return 128
	else:
		if h <= 30 or h >=225:
			return 255
		else:
			return 0
