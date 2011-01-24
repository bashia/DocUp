# /usr/bin/env python
# m2h.py- a script that uses Markdown to make HTML 4 files from plaintext
# files in Markdown format and zip them up for uploading to pypi.
#
# See the Readme for pre-requisites and install info.
#
# In the future, support will be added for multiple files and automatic
# uploading to pypi.
#
# Author: Anthony Darius Bashi
# email: bashia@uvic.ca

import sys
import os

def readargs():				# readargs gets all the command-line
	if (len(sys.argv) < 2):		# arguments and returns them in a list
		print "Usage: m2h [FILE1,FILE2,...]"	# More command-line args
	else:						# may be added in the future
		return sys.argv[1:]

def getfiles():				# getfiles returns a list of the filenames
	return readargs()[0].split(",")	# given in the command-line arguments

def downmark(filename):		# downmark uses markdown on a file filename
	cond = ""		# and, with some mild bash and python trickery,
	if (filename[0]=="-"):	# results in an html file with the same name
		cond = "--"	# minus the original extension plus '.html'

	newfilename = filename.split(".")[0] + ".html"

	formatting = "markdown " + cond + " " + filename + " -o html4" + " >> " + newfilename

	os.system(formatting)

	return newfilename


def zipup(filename):			# zipup simply uses gzip on a file filename
	formatted = "gzip " + filename

	os.system(formatted)

def multifile():			# multifile just downmarks and zipups
	for phile in getfiles():	# all the files named in the list 
		zipup(downmark(phile))	# returned by getfiles()
	

def main():

	multifile()

if __name__ == "__main__":
    main()
