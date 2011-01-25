# !/usr/bin/env python

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
	if (len(sys.argv) < 3):		# arguments and returns them in a list
		print "Usage: m2h [FILE1,FILE2,...] <archive-name>"	# More command-line args
	else:						# may be added in the future
		return sys.argv[1:]

def getfiles():				# getfiles returns a list of the filenames
	return readargs()[0].split(",")	# given in the command-line arguments

def downmark(filename):		# downmark uses markdown on a file filename
	cond = ""		# and, with some mild trickery,
	if (filename[0]=="-"):	# results in an html file with the same name
		cond = "--"	# minus the original extension plus '.html'

	newfilename = filename.split(".")[0] + ".html"

	formatting = "markdown " + cond + " " + filename + " -o html4" + " >> " + newfilename

	os.system(formatting)

	return newfilename	# downmark returns the name of the new html file for use by other functions


def movefile(filename):			# movefile simply moves file filename to /tmp/smoooog for zipping
	formatted = "mv " + filename + " /tmp/smoooog"

	os.system(formatted)

def fileops():				# fileops performs the file and directory movement and deletion
					# necessary before anything can be zipped
	os.system("rm -rf /tmp/smoooog")	#Removes any previous smoooogs that might get in the way
	os.system("mkdir /tmp/smoooog")		
	for phile in getfiles():		#This moves all the files that downmark has converted to /tmp/smoooog
		movefile(downmark(phile))

def zipify():				# zipify zips /tmp/smoooog's contents into a .zip file named in the
					# arguments and moves the .zip file to the user's working directory.
	archname = sys.argv[2]
	origdir = os.getcwd()
	zipdir = "cd /tmp/smoooog;" + " zip -r " + archname + " *" + "; mv " + archname + ".zip " + origdir
	os.system(zipdir)

def main():		
	fileops()
	zipify()
	

if __name__ == "__main__":
    main()
