from ij import IJ
from ij import ImagePlus
from ij.process import FloatProcessor
from ij.process import ByteProcessor
from ij.process import ImageConverter
from ij.plugin import ChannelSplitter
from array import zeros

# Getting the information
imp = IJ.getImage()
width = imp.width
height = imp.height
channels = ChannelSplitter.split(imp)
impRed = channels[0]
impGreen = channels[1]
impBlue = channels[2]

# Get Image Processors
ipRed = impRed.getProcessor().convertToFloat()
redPixels = ipRed.getPixels()
ipGreen = impGreen.getProcessor().convertToFloat()
greenPixels = ipGreen.getPixels()
ipBlue = impBlue.getProcessor().convertToFloat()
bluePixels = ipBlue.getPixels()

#rPixelCount = 0

# create a new array
maskPixels = zeros('f', width * height)


# identify red
for i in xrange(width):
	for j in xrange(height):
		# Calculate chromaticity coefficients
		if redPixels[(i*j)+j] != 0:
			x = redPixels[(i*j)+j]/(redPixels[(i*j)+j] + greenPixels[(i*j)+j] + bluePixels[(i*j)+j])
			y = greenPixels[(i*j)+j]/(redPixels[(i*j)+j] + greenPixels[(i*j)+j] + bluePixels[(i*j)+j])
			z = bluePixels[(i*j)+j]/(redPixels[(i*j)+j] + greenPixels[(i*j)+j] + bluePixels[(i*j)+j])
			# Edit mask
			maskPixels[(i*j)+j] = int(x * 255)
			#rPixelCount = rPixelCount + 1
		else:
			maskPixels[(i*j)+j] = 0

ip2 = FloatProcessor(width, height, maskPixels)
imp2 = ImagePlus("RedHue", ip2)
ic = ImageConverter(imp2)
ic.convertToGray8()
imp2.show()
#print "Red pixel count:" + str(rPixelCount)
#pixels = imp.getPixel(1608,412);
