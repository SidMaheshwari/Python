#file location /Users/Siddhanth/Desktop/python/Removecursewords
import urllib
import sys

def read_text():
	input_file = raw_input("The location of the file is: ")
	try:
		mytext = open(input_file, 'r')
		contents = mytext.read()
		mytext.close()
		check_profnity(contents)
	except: 
		print("Something went wrong")
		sys.exit()

def check_profnity(texty):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + texty) #returns true if profanity is found 
	output = connection.read()

	connection.close()

	if "false" in output:
		print("No curse words my sir/ma'am!")
	elif "true" in output:
		print("Shit man! There is a curse word in the document")	
	else:
		print("Oops! Error present!")
 
read_text()	