from ij.gui import GenericDialog

def getOptions():  
	item = ["coraline", "tunicate", "macro", "red", "more than one", "background"]
	gd = GenericDialog("Options")  
	gd.addRadioButtonGroup("options", item, 3, 2, "coraline")
	gd.showDialog()  
	
	if gd.wasCanceled():   
		return 0
	
	button = gd.getNextRadioButton()
	
	if button == "coraline":
		print button
		print 1
	elif button == "tunicate":
		print button
		print 1
	elif button == "macro":
		print button
		print 1
	elif button == "red":
		print button
		print 1
	elif button == "more than one":
		print button
		print 1
	elif button == "background":
		print button
		print 1
	else:
		print 0
	return

getOptions()