# Title: FileFunctions.py
# Author: Juliana Hernandez
# Description: File functions for UrchinPy

print "Imported FileFunctions.py..."

# Python Libraries
import os
import csv

# Name: initializeCSV
# Inputs: timeStr - string containing time and date to name CSV file
#		  fdest - destination directory of file
# Output: newPath - pathfile to the CSV being used to save the information
def initializeCSV(timeStr, fdest):

	# new path for naming file
	newPath = fdest + "\\" + timeStr + ".csv"
	
	doc = os.path.basename(newPath)
	if not os.path.isfile(newPath):
		#print "True"
#	else:
		#print "False"
		# create CSV file
		with open(newPath, 'wb') as csvfile:
			filewriter = csv.writer(csvfile, delimiter=',') # , quotechar='', quoting = csv.QUOTE_MINIMAL
			filewriter.writerow(['Filename', 'Site', 'Date Collected', 'Sample#', 'Photo#', 'Date Processed', 'Total Pixel Num', 'Coraline Pixel Num', 'Turnicate Pixel Num', 'Red Pixel Num', 'Macro Pixel'])

	# Return CSV filepath
	return newPath

# insert new line
# is currently overwriting rows
# Name: appendNewRow
# Inputs: fname - pathfile to the CSV being used to save the information
#		  pname - name of image analyzed
#		  currentTime - current time
#		  totalPix - total pixels
#         corralinePix - total corraline pixels
#		  turnicatePix - total turnicate pixels
#		  redPix - total red macro pixels
#		  greenPix - total green algae pixels
# Output: 
def appendNewRow(fname ,pname, currentTime, data):
	# get file name information
	doc = os.path.basename(pname) # file name
	temp = doc.split('.', 2)
	photoNum = temp[1] # Photo number
	info = temp[0].split('_') # list of tokenized title
	siteName = info[0] # Site name
	dateCollected = info[1] # Date collected
	# Reseape the date to YYYY-MM-DD
	YYYY = '20' + dateCollected[0:2]
	MM = dateCollected[2:4]
	DD = dateCollected[4:6]
	dateReshaped = str(YYYY) + '-' + str(MM) + '-' + str(DD)
	# check to see if "500" is included in the title
	if info[2] == "500":
		sampleNum = info[3]
	else:
		sampleNum = info[2]
	with open(fname, 'ab') as csvfile:
		filewriter = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting = csv.QUOTE_MINIMAL) # 
		# ['Filename', 'Site', 'Date Collected', 'Sample#', 'Photo#', 'Date Processed', 'Total Pixel Num', 'Coraline Pixel Num', 'Turnicate Pixel Num', 'Red Pixel Num', 'Green Pixel']
		filewriter.writerow([str(doc), str(siteName), str(dateReshaped), str(sampleNum), str(photoNum), str(currentTime), data])

def formatData(coralline, tunicate, red, macro):
	total = coralline + tunicate + red + macro
	formattedStr = str(total) + "," + str(coralline) + "," + str(tunicate) + "," + str(red) + "," + str(macro)
	return formattedStr