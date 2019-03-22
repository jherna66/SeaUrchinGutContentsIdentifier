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

redMean = sum(redPixels) / len(redPixels)
greenMean = sum(greenPixels) / len(greenPixels)
blueMean = sum(bluePixels) / len(bluePixels)

print redMean
print greenMean
print blueMean



redNew = map(lambda x: x * redMean, redPixels)
greenNew = map(lambda x: x * greenMean, greenPixels)
blueNew = map(lambda x: x * blueMean, bluePixels)

maxes = zeros('f', 3)

maxes[0] = reduce(max, redNew)
maxes[1] = reduce(max, greenNew)
maxes[2] = reduce(max, blueNew)

maximum = 0
for index in maxes:
	if index > maximum:
		maximum = index

print maximum

redIt = map(lambda x: (x / maximum) * 255, redNew)
greenIt = map(lambda x: (x / maximum) * 255, greenNew)
blueIt = map(lambda x: (x / maximum) * 255, blueNew)

ip1 = FloatProcessor(width, height, redIt)
ip2 = FloatProcessor(width, height, greenIt)
ip3 = FloatProcessor(width, height, blueIt)

imp1 = ImagePlus("RedNew", ip1)
imp2 = ImagePlus("GreenNew", ip2)
imp3 = ImagePlus("BlueNew", ip3)

ic1 = ImageConverter(imp1)
ic2 = ImageConverter(imp2)
ic3 = ImageConverter(imp3)

ic1.convertToGray8()
ic2.convertToGray8()
ic3.convertToGray8()

imp1.show()
imp2.show()
imp3.show()
