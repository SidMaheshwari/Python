#Run with python 2
import os
import string 

def rename_files():
    file_list =  os.listdir("/Users/Siddhanth/Desktop/Prank") #file folder, In this case it was on my desktop

    os.chdir("/Users/Siddhanth/Desktop/Prank")   #file folder, In this case it was on my desktop
    for file in file_list:
        os.rename(file,file.translate(None,"1234567890"))
        
rename_files()
