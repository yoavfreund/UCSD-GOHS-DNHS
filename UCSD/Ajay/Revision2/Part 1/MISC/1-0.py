# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:18:48 2013

@author: anonymous
"""
#opens the file in a read only state
file = open("./w1010.txt", 'r')
#creates variable output
output = ""
last1 = "na"
last2 = "na"
last3 = "na"
last4 = "na"
#tabs keeps track of what section the program is focussed on in each line
tabs = 1
for line in file.readlines():
    for section in line.split('|'):
        if tabs >= 6:
            print "-"
        elif tabs == 1:
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