#compatible with Python 2

#Imports needed libraries (part 1)
import glob
import os

#defines variables
trueDir = False
output = ""
last1 = ""
last2 = ""
last3 = ""
last4 = ""
last5 = ""
newstring = []
noDup = []

#Number testing statement for Daniel's code (part 1)
def is_number(s):                                         #Returns False if s is not numerical
    try:
        float(s) 
        return True 
    except ValueError:
        return False

#Daniel's code to emit uneeded idex numbers (part 1)
def push_extra(TEXTFILE):
    finalFilter = ""
    filterOUT = open("filterOUT.txt", mode="w")
    for line in TEXTFILE:                                 #line by line reading
        for data in line.split('|'):
            isempty = 0
            for word in data.split(' '):                  #Splits words up after splitting the sections
                if (is_number(data)) and (len(word) < 3): #IMPORTANT: cheks to see if the section is numerical, and if any number is 2 digits or less
                    data.replace(data, '')
                    print "Replacing."
                    #newstring.append(data)               #uncomment to see the specific categorical designation numbers
                else:
                    isempty +=1
                    newstring.append(word + " ")
            if isempty > 0:
                newstring.append("|")
        newstring.append("\n")
        print "#Next line"
    #filterOUT.write(str(newstring))
    for numb in newstring:
        finalFilter = finalFilter + numb
    filterOUT.write(finalFilter)

#Recieve and test directory given by user
while trueDir == False:
    directory = raw_input("Please enter valid directory to search: ")
    if os.path.exists(directory):
        trueDir = True
    else:
        print("Invalid directory")

#Makes directory = user inputted directory (NOTE: NOT LINUX FORMAT DIRECTORY)
os.chdir(directory)

#opens target.txt
target = open("target.txt", mode="w")

for files in glob.glob("w1*.txt"):
    target.write(files + "\n")
    print files

target.close()

#opens target.txt for reading
targetr = open("target.txt", mode="r")
#opens output file for appending
out = open("output.txt", mode="a")


for line in targetr.readlines(): #loops through filenames to test
    filename = line[:-1] #creates string of filename by cutting \n off line
    inp = open(filename, mode = "r") #opens files to test
    tabs = 0 #Will's code
    #####################################
    push_extra(inp)
    filterIN = open("filterOUT.txt", mode = 'r')
    for line in (filterIN).readlines():
        if len(line) > 10:
            for section in line.split('|'):
                if tabs == 0:
                    if last1 != section:
                        output = output + section + "\n"
                        last1 = section
                elif tabs == 1:
                    if last2 != section:
                        output = output + "    " + section + "\n"
                        last2 = section
                elif tabs == 2:
                    if last3 != section:
                        output = output + "        " + section + "\n"
                        last3 = section
                elif tabs == 3:
                    if last4 != section:
                        output = output + "            " + section + "\n"
                        last4 = section
                elif tabs == 4:
                    if last5 != section:
                        output = output + "                " + section + "\n"
                        last5 = section
                elif tabs == 5:
                    output = output + section + "\n"
                tabs += 1
                """
                #prototype
                try:
                    if section != str(noDup[tabs]):
                        countDWN = tabs
                        while countDWN > 0:
                            output = output + "    "
                            countDWN = countDWN - 1
                        output = output + section + "\n"
                        noDup[tabs: tabs + 1] = [section]
                except:
                    countDWN = tabs
                    while countDWN > 0:
                        output = output + "    "
                        countDWN = countDWN - 1
                    output = output + section + "\n"
                    noDup[tabs: tabs + 1] = [section]
                tabs +=1
                """
            tabs = 0
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