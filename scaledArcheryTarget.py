#!/usr/bin/python

import sys
import getopt
import os

def main(argv):
# some defaults and useful constants
	diameter = 400.0
	lineWidth = None
	lineWidthRatio = 1000.0
	maxLineWidth = 1.0
	crossLength = None
	crossLengthRatio = 50.0
	maxCrossLength = 4.0
	vegas = False
	rowCount = 1
	lineCount = 1
	centerOnly = False
	numbered = False
	outputFile = None
	omitTen = False
	omitX = False
	output = ""
	gold = "#FFE552"
	red = "#F65058"
	blue = "#00B4E4"
	black = "#000000"
	white = "#FFFFFF"
	
	helpString = "useage scaledArcheryTarget.py [-dowrlvcntxh]\n\n\
	-d <diameter>\t\t: Diameter in mm, defaults to 400mm if unspecified\n\
	-o <output file>\t: File Name, defaults to target-diameter.  Will have .svg appended automatically\n\
	-w <line width>\t\t: Line Width, defaults to diameter/1000 max 1mm\n\
	-r <number of targets>\t: A vertical row of targets, creates a block of targets when specified with -l\n\
	-l <number of targets>\t: a horizontal line of targets, creates a block of targets when specified with -r\n\
	-v\t\t\t: Vegas Style Triangular Target, best used with Target Centers\n\
	-c\t\t\t: Target Center Only\n\
	-n\t\t\t: Print Numbers for scoring\n\
	-t\t\t\t: Omit Ten ring (for indoor compound targets)\n\
	-x\t\t\t: Omit X ring (for indoor recurve targets)\n\
	-h\t\t\t: Print Useage Information\n"
# parse the opts, poorly	
	try:
		opts, args = getopt.getopt(argv,"d:o:w:r:l:vcvntxh",["d=","ofile=","width="])
	except getopt.GetoptError:
		print helpString
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print helpString
			sys.exit()
		elif opt in ("-d", "--diameter"):
			diameter = int(arg)
		elif opt in ("-o", "--ofile", "--output"):
			outputFile = arg
		elif opt in ("-w", "--width"):
			lineWidth = float(arg)
		elif opt in ("-r", "--row"):
			rowCount = int(arg)
		elif opt in ("-l", "--line"):
			lineCount = int(arg)
		elif opt in ("-v", "--vegas"):
			vegas = True
		elif opt in ("-c", "--centeronly"):
			centerOnly = True
		elif opt in ("-n", "--numbered"):
			numbered = True
		elif opt in ("-t", "--tenomit"):
			omitTen = True
		elif opt in ("-x", "--xomit"):
			omitX = True
	
	if not outputFile:
		outputFile = "target-" + str(diameter/10) +"cm"
		if vegas:
			outputFile += "-vegas"
		elif lineCount>1 or rowCount>1:
			outputFile += "-" + str(lineCount)+ "x" + str(rowCount)
		if centerOnly:
			outputFile += "-center"
		if numbered:
			outputFile += "-numbered"
	if not lineWidth:
		lineWidth = min(diameter / lineWidthRatio,maxLineWidth)
#		output += "<!--calculated line width is " + str(lineWidth) + "-->\n"
	crossLength = min(diameter/crossLengthRatio,maxCrossLength)
#	output += "<!--calculated cross length is " + str(crossLength) + "-->\n"
	
	if vegas:
		sizeX = diameter * 2
		sizeY = diameter * 1.866
	else:
		sizeX = diameter * lineCount
		sizeY = diameter * rowCount
	midpoint = diameter/2.0
	step = midpoint/10.0
	output += "<svg" + os.linesep
	output += "version=\"1.1\"" + os.linesep
	output += "xmlns=\"http://www.w3.org/2000/svg\"" + os.linesep
	output += "xmlns:xlink=\"http://www.w3.org/1999/xlink\"" + os.linesep
	output += "xml:space=\"preserve\"" + os.linesep
	
	if centerOnly:
		output += "height=\"" + str(sizeY/2) + "mm\"" + os.linesep
		output += "width=\"" + str(sizeX/2) + "mm\"" + os.linesep
		midpoint /= 2
	else:
		output += "height=\"" + str(sizeY) + "mm\"" + os.linesep
		output += "width=\"" + str(sizeX) + "mm\"" + os.linesep
	output += ">" + os.linesep + os.linesep
	
	output += "<defs> + os.linesep" + os.linesep
	output += "<g id=\"target\">" + os.linesep
	
	if not centerOnly:
		output += "<!--One Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*0) + "mm\" fill=\""+black+"\"/>" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*0-lineWidth) + "mm\" fill=\""+white+"\"/>" + os.linesep
	
		output += "<!--Two Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*1) + "mm\" fill=\""+black+"\"/>" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*1-lineWidth) + "mm\" fill=\""+white+"\"/>" + os.linesep
	
	
		output += "<!--Three Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*2) + "mm\" fill=\""+black+"\"/>" + os.linesep
	
		output += "<!--Four Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*3) + "mm\" fill=\""+white+"\"/>" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*3-lineWidth) + "mm\" fill=\""+black+"\"/>" + os.linesep
	
	
		output += "<!--Five Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*4) + "mm\" fill=\""+blue+"\"/>" + os.linesep
	
	output += "<!--Six Circle-->" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*5) + "mm\" fill=\""+black+"\"/>" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*5-lineWidth) + "mm\" fill=\""+blue+"\"/>" + os.linesep
	
	output += "<!--Seven Circle-->" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*6) + "mm\" fill=\""+black+"\"/>" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*6-lineWidth) + "mm\" fill=\""+red+"\"/>" + os.linesep
	
	output += "<!--Eight Circle-->" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*7) + "mm\" fill=\""+black+"\"/>" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*7-lineWidth) + "mm\" fill=\""+red+"\"/>" + os.linesep
	
	output += "<!--Nine Circle-->" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*8) + "mm\" fill=\""+black+"\"/>" + os.linesep
	output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*8-lineWidth) + "mm\" fill=\""+gold+"\"/>" + os.linesep
	
	if not omitTen:
		output += "<!--Ten Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*9) + "mm\" fill=\""+black+"\"/>" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*9-lineWidth) + "mm\" fill=\""+gold+"\"/>" + os.linesep
	
	if not omitX:
		output += "<!--X Circle-->" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*9.5) + "mm\" fill=\""+black+"\"/>" + os.linesep
		output += "<circle cx=\"" + str(midpoint) + "mm\" cy=\"" + str(midpoint) + "mm\" r=\"" + str(diameter/2-step*9.5-lineWidth) + "mm\" fill=\""+gold+"\"/>" + os.linesep
	
	output += "<!--Cross-->" + os.linesep
	output += "<rect width=\""+str(crossLength)+"mm\" height=\""+str(lineWidth)+"mm\" x=\""+str(midpoint-crossLength/2)+"mm\" y=\""+str(midpoint-lineWidth/2)+"mm\" fill=\""+black+"\"/>" + os.linesep
	output += "<rect width=\""+str(lineWidth)+"mm\" height=\""+str(crossLength)+"mm\" x=\""+str(midpoint-lineWidth/2)+"mm\" y=\""+str(midpoint-crossLength/2)+"mm\" fill=\""+black+"\"/>" + os.linesep
	
	if numbered:
		xStep = diameter/20
		xPos = midpoint + xStep/2
		yPos = midpoint + (diameter/200)
		fontSize = diameter/50
		i = 10
		output += os.linesep
		output += "<!--numbers-->" + os.linesep
		if centerOnly:
			stop = 5
		else:
			stop = 0
		for i in range(10,stop,-1):
			if i is not 10 or not omitTen:
				output += "<text x=\"" + str(xPos) + "mm\" y=\"" + str(yPos) + "mm\" fill=\""
				if i is 3 or i is 4:
					output += white
				else:
					output += black
				output += "\" font-size=\"" + str(fontSize) + "mm\">" + str(i) + "</text>" + os.linesep
			xPos += xStep
			i -= 1
	output += "</g> + os.linesep" + os.linesep
	output += "</defs>" + os.linesep
	
	if centerOnly:
		diameter /= 2
	
	if vegas:
		output += "<use xlink:href=\"#target\" x=\""+str(diameter*0.5)+"mm\" y=\""+str(diameter*0)+"mm\"/>" + os.linesep
		output += "<use xlink:href=\"#target\" x=\""+str(diameter*0)+"mm\" y=\""+str(diameter*0.866)+"mm\"/>" + os.linesep
		output += "<use xlink:href=\"#target\" x=\""+str(diameter*1)+"mm\" y=\""+str(diameter*0.866)+"mm\"/>" + os.linesep
	else:
		for x in range(lineCount):
			for y in range(rowCount):
				output += "<use xlink:href=\"#target\" x=\""+str(diameter*x)+"mm\" y=\""+str(diameter*y)+"mm\"/>" + os.linesep

	output += "</svg>"
	if outputFile is None:
		print output
	else:
		f = open(outputFile+".svg", 'w')
		f.write(output)
		f.close()


if __name__ == "__main__":
   main(sys.argv[1:])