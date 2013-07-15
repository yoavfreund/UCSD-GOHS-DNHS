import os

PATH = r'/Users/Ajay/Documents/Python/Test' #change the code inside the ' ' to the folder location
#^^^!!keep the r!!

for file in os.listdir(PATH): #os.listdir(PATH) lists all files within the folder 
    if os.path.isfile(f) and f.startswith('test'): #checks that file is only a file (not a folder or something)
        #change 'test' to desired file's beginning (ex. 'w1010')
        print f #prints file name
    else: #else statement can be deleted
        print "No" 
