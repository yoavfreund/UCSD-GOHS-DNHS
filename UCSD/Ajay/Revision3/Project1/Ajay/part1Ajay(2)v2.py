#compatible with Python 2

import glob
import os #imports needed directories and glob

trueDir = False #defines variables
output = ""
last1 = ""
last2 = ""
last3 = ""
last4 = ""
last5 = ""

while trueDir == False:
    #directory = input("Please enter valid directory to search: ") #use input for Python 3
    directory = raw_input("Please enter valid directory to search: ")
    if os.path.exists(directory):
        trueDir = True
    else:
        print("Invalid directory") #loops to get valid directory from user

os.chdir(directory) #working directory is now one being searched

target = open("target.txt", mode="w") #opens target.txt

for files in glob.glob("w1*.txt"):
    #print(files, file = target)  #writes filenames to test into target.txt
    target.write(files + "\n")

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
                if last5 != section:
                    output = output + "                " + section + ": "
                    last5 = section
            elif tabs == 6:
                output = output + section + "\n"
            tabs += 1
        tabs = 1
    #print("\n" + filename + "\n", file = out) #prints filename
    out.write("\n" + filename + "\n\n")
    #print(output, file = out) #prints output
    out.write(output)
    output = "" #resets variables
    last1 = ""
    last2 = ""
    last3 = ""
    last4 = ""
    inp.close()

print("done")

#need too apply to Richard's code
#need to find way to search subdirectories

