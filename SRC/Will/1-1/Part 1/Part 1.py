# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:18:48 2013

@author: anonymous
"""


"""
PREPARATION
"""

#import needed libraries
import os

#sets up needed variable
textList = ""
    #Variable to determine if the directory the user inputted was valid
trueDir = False
    #variable to be written to output.txt
output = ""
    #string to be replaced later with name of section 1
last1 = "na"
    #string to be replaced later with name of section 2
last2 = "na"
    #string to be replaced later with name of section 3
last3 = "na"
    #string to be replaced later with name of section 4
last4 = "na"
    #opens the file in a read only state
    
#gathers user directory
while trueDir == False:
    directory = raw_input("Please enter valid directory to search: ")
    try:
        testDir = os.listdir(directory)
        trueDir = True
    except:
        print "Invalid directory"

#creates method to search
def searchMaster(route):
    PATH = r'%s' % (route)
    for file in os.listdir(PATH):
        f = file
        if os.path.isfile(f) and f.startswith('w1'):
            textList = route + f + ".txt" + "/" + "\n"
        elif os.path.isdir(f):
            curPath = route + f + '/'
            current = searchMaster(curPath)
            curPath = current
print textList
"""
CODE
"""          
searchMaster(directory)
"""   
file = open("./MockFolder/w1010.txt", 'r')
#creates variable output
#tabs keeps track of what section the program is focussed on in each line
tabs = 1
for line in file.readlines():
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
        tabs +=1
    tabs = 1
file = open("./output.txt", 'w')
file.write(output)
print 'done'
"""