import os
import string 

def rename_files():
    file_list =  os.listdir("/Users/Siddhanth/Desktop/Prank")
    #print(file_list)
    os.chdir("/Users/Siddhanth/Desktop/Prank")
    for file in file_list:
        os.rename(file,file.translate(None,"1234567890"))
        
rename_files()
