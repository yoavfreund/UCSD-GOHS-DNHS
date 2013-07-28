# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

                    

# <codecell>

"""This part of the code eliminates unnecessary section numbers,, so far it seems as if there are only 59 section numbers, 
but it works for numbers less than 99"""
import re 

w1010 = open("data/w1010.txt", 'r')      #CHANGE TO CORRECT PATHWAY!
w1010txt = w1010.readlines()[0:100]                                        #first 10 lines, verify that it works with all lines by ommiting the 10

w1020 = open("data/w1020.txt", 'r')   #CHANGE TO CORRECT PATHWAY!
w1020txt = w1020.readlines()[0:10]

index = open("output/index.html", "w")

#print w1010txt                                                             #Troubleshooting purposes
#print w1020txt

newstring = []   #CHANGE, can only contain one file's data at a time, perhaps rewrite so that each file gets a unique variable?

def beginHTML():
    index.write("<!DOCTYPE html><html><head>")
    index.write("<title>Census Tables</title>")
    index.write("<meta charset=\"UTF-8\">")
    index.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">")
    index.write("</head><body>")

def endHTML():
    index.write("</body></html>")
    
def writeCSS():
    css = open("style.css", "w")
    css.write("/*stylesheet for use if necessary*/")    #replace CSS comment in write() with style rules if desired

def is_number(s):                                         #Returns False if s is not numerical
    try:
        float(s) 
        return True 
    except ValueError:
        return False

def push_extra(TEXTFILE):
    for line in TEXTFILE:                                 #line by line reading
        for data in line.split('|'):#Splits words up after splitting the sections
            if (is_number(data)) and (len(data) < 5): #IMPORTANT: cheks to see if the section is numerical, and if any number is 2 digits or less
                    data.replace(data, '')                #note that this doesn't do anyinght because strings are immutable
                    #print "true"                         #For troubleshooting purposes
                    #newstring.append(data)               #uncomment to see the specific categorical designation numbers
            else:
                    #print "error"                        #For troubleshooting purposes
                newstring.append(data)
            

push_extra(w1010txt)            
#print newstring
#for numb in newstring:
   # print numb,
    
    
newstring = []
    
    
push_extra(w1020txt)            
#print newstring
#for numb in newstring:
#    print numb,


def row_major(alist, sublen):      
  return [alist[i:i+sublen] for i in range(0, len(alist), sublen)]
  
def html_table(lol):
  index.write('<table border="1">')
  for sublist in lol:
    index.write('  <tr><td>')
    index.write('    </td><td>'.join(sublist))
    index.write('  </td></tr>')
  index.write('</table>')
  
  
html_ready = row_major(newstring, 9) 
#for r in row_major(newstring, 9): print r

beginHTML()
#writeCSS()
html_table(html_ready)
endHTML()

#import time    
#start = time.time()
#b = [push_extra(w1020txt)]
#print time.time() - start #check to see how fast the function works!    

# <codecell>


# <codecell>


