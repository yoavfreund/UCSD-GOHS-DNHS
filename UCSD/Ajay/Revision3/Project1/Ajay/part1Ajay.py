#compatible with Python 3

import glob
import os #imports needed directories and glob

trueDir = False #defines variables
output = ""
last1 = ""
last2 = ""
last3 = ""
last4 = ""

while trueDir == False:
    directory = input("Please enter valid directory to search: ") #use raw_input for Python 2
    if os.path.exists(directory):
        trueDir = True
    else:
        print("Invalid directory") #loops to get valid directory from user

os.chdir(directory)

target = open("target.txt", mode="w") #opens target.txt

for files in glob.glob("w1*.txt"):
    print(files, file = target)  #writes filenames to test into target.txt

target.close()

targetr = open("target.txt", mode="r") #opens target.txt for reading
out = open("output.txt", mode="a") #opens output file for appending --
#output for all files to be tested sent to one file

for line in targetr.readlines(): #loops through filenames to test
    filename = line[:-1] #creates string of filename by cutting \n off line
    inp = open(filename, mode = "r") #opens files to test
    tabs = 1 #Will's code
    for line in inp.readlines():
        for section in line.split('|'):
            if tabs == 1:
                if last1 != section:
                    output = output + section + "\n"
                    last1 = section
            elif tabs == 2:
                if last2 != section:
                    output = output + "    " + section + "\n"
                    last2 = section
            elif tabs == 3:
                if last3 != section:
                    output = output + "        " + section + "\n"
                    last3 = section
            elif tabs == 4:
                if last4 != section:
                    output = output + "            " + section + ": "
                    last4 = section
            elif tabs == 5:
                output = output + section + "\n"
            tabs += 1
        tabs = 1
    print("\n" + filename + "\n", file = out) #prints filename 
    print(output, file = out) #prints output
    output = "" #resets variables
    last1 = ""
    last2 = ""
    last3 = ""
    last4 = ""
    inp.close()

print("done")
