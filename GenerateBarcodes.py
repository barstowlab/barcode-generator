#!/sw/bin/python2.7


# ------------------------------------------------------------------------------------------------ #
def GenerateCheckSum(text):
	import numpy
	
	textArray = []
	ordArray = []
	subtractionArray = []
	
	for letter in text:
		textArray.append(letter)
		ordArray.append(ord(letter))
		subtractionArray.append(ord(letter) - 55)
		
	j = 0
	checksum = 0
	subtractionArrayCopy = numpy.zeros(8, numpy.int)

	while j < min([len(subtractionArray), 8]):
		subtractionArrayCopy[j] = subtractionArray[j]
		j += 1
	
	j = 0
	while j < min([len(subtractionArray), 8]):
		if subtractionArrayCopy[j] < 10:
			subtractionArrayCopy[j] += 7
		checksum += subtractionArrayCopy[j]
		j += 1
	
	checksumMod = checksum%36
	if checksumMod < 10:
		checksumMod -= 7
	checkcar = chr(checksumMod+55)
	
	#return [textArray, ordArray, subtractionArray, subtractionArrayCopy, checksum, \
	#checksumMod, checkcar]
	
	return checkcar
# ------------------------------------------------------------------------------------------------ #








import numpy

outputFile = "Test.csv"

delimeter = ","
lineBreak = "\n"

prefix = "Test"
postfix = ""

# For the Avery clear 15667 labels, you have a grid of 4x20 labels.

MaxRows = 20
MaxColumns = 4

# This is the number of labels that you want to make. 
TotalLabels = 8

PaddingColumns = True
PaddingRows = False

sampleNumbers = numpy.arange(1,3)
replicaNumbers = numpy.arange(1,5)



# ------------------------------------------------------------------------------------------------ #
# Generate the sample labels
sampleIDs = []
for number in sampleNumbers:
	for replica in replicaNumbers:	
		sampleID = prefix + str(number) + 'v' + str(replica)
		sampleIDs.append(sampleID)
# ------------------------------------------------------------------------------------------------ #


# ------------------------------------------------------------------------------------------------ #
labels = []
for sampleID in sampleIDs:
	barcode = sampleID + GenerateCheckSum(sampleID)
	labels.append("*" + barcode + "*")
# ------------------------------------------------------------------------------------------------ #

TotalLabels = min([len(labels), TotalLabels])




# ------------------------------------------------------------------------------------------------ #
row = 1
column = 1
labelCount = 1


rowData = []

while row <= MaxRows:
	rowText = ""
	
	column = 1
	while column <= MaxColumns and labelCount <= TotalLabels:
		label = labels[labelCount-1]
		labelCount += 1
		
		if column < MaxColumns:
			rowText += label + delimeter
			if PaddingColumns == True:
				rowText += delimeter
		else:
			rowText += label + lineBreak
			if PaddingRows == True:
				rowText += lineBreak
				
		column += 1
		
	rowData.append(rowText)
	row += 1
# ------------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------------ #
# Output the row data

fileHandle = open(outputFile, 'w')
for row in rowData:
	fileHandle.write(row)
	
fileHandle.close()
# ------------------------------------------------------------------------------------------------ #

