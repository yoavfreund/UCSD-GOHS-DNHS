import glob
import os

out = open("output.txt", mode="w") #open output file for writing

os.chdir("/Users/Ajay/Documents/Python/Test") #replace with your path

for files in glob.glob("test*.txt"):
    print(files, file = out)

out.close()

#^^loops through and prints name of txt files that start with "test",
#the * is placeholder for anything that follows "test"
#change condition in glob.glob("yourCondition")

#possible way to integrate:
#   open output file for reading to get filenames
#   loop through each line of file (each line is a filename)
#   open file whose name is currently being looped through
#   run program as desired
#   (original program is contained in loop)
