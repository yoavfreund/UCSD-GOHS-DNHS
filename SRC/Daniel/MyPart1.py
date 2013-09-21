# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

                    

# <codecell>

"""This part of the code eliminates unnecessary section numbers,, so far it seems as if there are only 59 section numbers, 
but it works for numbers less than 99"""
import re 

w1010 = open(".\w1010.txt", 'r')      #CHANGE TO CORRECT PATHWAY!
w1010txt = w1010.readlines()[0:10]                                         #first 10 lines, verify that it works with all lines by ommiting the 10

w1020 = open("C:\Users\Daniel\Desktop\UCSD resources\w1020.txt", 'r')
w1020txt = w1020.readlines()[0:10]


#print w1010txt                                                             #Troubleshooting purposes
#print w1020txt

newstring = [ ]   #CHANGE, can only contain one file's data at a time, perhaps reqwrite so that each file gets a unique variable?


def is_number(s):                                         #Returns False if s is not numerical
    try:
        float(s) 
        return True 
    except ValueError:
        return False

def push_extra(TEXTFILE):
    for line in TEXTFILE:                                 #line by line reading
        for data in line.split('|'):
            for word in data.split(' '):                  #Splits words up after splitting the sections
                if (is_number(data)) and (len(word) < 3): #IMPORTANT: cheks to see if the section is numerical, and if any number is 2 digits or less
                    data.replace(data, '')                #note that this doesn't do anyinght because strings are immutable
                    #print "true"                         #For troubleshooting purposes
                    #newstring.append(data)               #uncomment to see the specific categorical designation numbers
                else:
                    #print "error"                        #For troubleshooting purposes
                    newstring.append(word)
            

push_extra(w1010txt)            
#print newstring
for numb in newstring:
    print numb,
    
    
newstring = []
    
    
push_extra(w1020txt)            
#print newstring
for numb in newstring:
    print numb,

    
#import time    
#start = time.time()
#b = [push_extra(w1020txt)]
#print time.time() - start #check to see how fast the function works!    

# <codecell>


# <codecell>


