from ij import IJ
from ij import ImagePlus
from ij.plugin import ChannelSplitter
#from array import zeros
#from ij.process import ImageProcessor

imp = IJ.getImage()
width = imp.width
print width
height = imp.height
print height

channels = ChannelSplitter.split(imp)

impRed = channels[0]
impRed.show()

impGreen = channels[1]
impGreen.show()

impBlue = channels[2]
impBlue.show()