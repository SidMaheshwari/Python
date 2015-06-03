#file location /Users/Siddhanth/Desktop/python/Removecursewords
import urllib
import sys
 
def write():
    print('Creating new text file') 

    name = raw_input('Enter name of text file: ')+'.txt' 

    try:
        file_name = open(name,'a') 

      	file_content = open_file()
      	file_output = pirate(file_content)
    	file_name.write(file_output)
        file_name.close()

    except:
        print('Something went wrong! Boohoo!')
        sys.exit(0)

def open_file():
	input_file = raw_input("The location of the file is: ")
	mytext = open(input_file, 'r')
	contents = mytext.read()
	mytext.close()
	return contents

def pirate(text):
	connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text)
	outputz = connection.read()
	connection.close()
	return output


write()



