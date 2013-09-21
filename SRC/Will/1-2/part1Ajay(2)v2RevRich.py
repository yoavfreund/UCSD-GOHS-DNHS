#compatible with Python 2

#Imports needed libraries (part 1)
import glob
import os

#rich
import string
allTheLetters = string.uppercase
banner = "------------------------------------------------------------------------------------------------------"

#rich methods
def read_headers():
     ins = open( "headers.txt", "r" )
     dict = {}
     for line in ins:
                # print line
                line = line.rstrip()
                line = line.lstrip()
                id, title = line.split(" ", 1)
                # print "Id: "  +  id  +  " Title:"  +  title
                dict[id] = title
        # print str(dict)
     return dict
def two_digit_pc(in1):
	if len(in1) == 1:
		in1 = " " + in1 + "%"
	if len(in1) == 2:
		in1 = in1 + "%"
	return 	in1
def by_sex_by_age_table_line(base_id, category, below, above):
        table_line= category + \
        two_digit_pc(str(int(data_dict[base_id][below])*100 / (int(data_dict[base_id][below])+int(data_dict[base_id][above])))) + "      "
        for a in allTheLetters:
                id = base_id+a
                if id in data_dict:
                        table_line = table_line + \
                two_digit_pc(str(int(data_dict[id][below])*100 / (int(data_dict[id][below])+int(data_dict[id][above])))) + "      "
        return table_line
def process_poverty_by_sex_by_age(title_dict, data_dict):
	base_id="B17001"
	print banner
	print title_dict[base_id] + " (Poverty Rate)"
	print banner
	print "           Total    White   African   Native  Asian   Islander    Other    >Two  Caucasian  Hispanic"
	table_line= "  Overall   "+two_digit_pc(str(int(data_dict[base_id]["2"])*100 / int(data_dict[base_id]["1"]))) + "      "
	for a in allTheLetters:
		id = base_id+a
		if id in data_dict:
			table_line = table_line +two_digit_pc(str(int(data_dict[id]["2"])*100 / int(data_dict[id]["1"]))) + "      "
	print table_line
	print by_sex_by_age_table_line(base_id, "  Male      ", "3", "32")
	print by_sex_by_age_table_line(base_id, "  <5        ", "4", "33")
	print by_sex_by_age_table_line(base_id, "  5         ", "5", "34")
	print by_sex_by_age_table_line(base_id, "  6-11      ", "6", "35")
	print by_sex_by_age_table_line(base_id, "  12-14     ", "7", "36")
	print by_sex_by_age_table_line(base_id, "  15        ", "8", "37")
	print by_sex_by_age_table_line(base_id, "  16-17     ", "9", "38")
	print by_sex_by_age_table_line(base_id, "  18-24     ", "10", "39")
	print by_sex_by_age_table_line(base_id, "  25-34     ", "11", "40")
	print by_sex_by_age_table_line(base_id, "  35-44     ", "12", "41")
	print by_sex_by_age_table_line(base_id, "  45-54     ", "13", "42")
	print by_sex_by_age_table_line(base_id, "  55-64     ", "14", "43")
	print by_sex_by_age_table_line(base_id, "  65-74     ", "15", "44")
	print by_sex_by_age_table_line(base_id, "  >75       ", "16", "45")	
	print by_sex_by_age_table_line(base_id, "  Female    ", "17", "46")
	print by_sex_by_age_table_line(base_id, "  <5        ", "18", "47")
	print by_sex_by_age_table_line(base_id, "  5         ", "19", "48")
	print by_sex_by_age_table_line(base_id, "  6-11      ", "20", "49")
	print by_sex_by_age_table_line(base_id, "  12-14     ", "21", "50")
	print by_sex_by_age_table_line(base_id, "  15        ", "22", "51")
	print by_sex_by_age_table_line(base_id, "  16-17     ", "23", "52")
	print by_sex_by_age_table_line(base_id, "  18-24     ", "24", "53")
	print by_sex_by_age_table_line(base_id, "  25-34     ", "25", "54")
	print by_sex_by_age_table_line(base_id, "  35-44     ", "26", "55")
	print by_sex_by_age_table_line(base_id, "  45-54     ", "27", "56")
	print by_sex_by_age_table_line(base_id, "  55-64     ", "28", "57")
	print by_sex_by_age_table_line(base_id, "  65-74     ", "29", "58")
	print by_sex_by_age_table_line(base_id, "  >75       ", "30", "59")
	return
def process_poverty_by_ratio_of_income(title_dict, data_dict):
        base_id="B17002"
        print banner
        print title_dict[base_id] + " (Poverty Distribution)"
        print banner
        print "  Income Ratio:      <  0.50   0.75   1.00   1.25   1.50   1.75   1.85   2.00   3.00   4.00   5.00  >"

	table_line = "  Poverty Distri.:   "
	for i in range(2,100):
		index = str(i);
		if index in data_dict[base_id]:	
			table_line +=  two_digit_pc(str(int(data_dict[base_id][index])*100 / int(data_dict[base_id]["1"])))+ "    "
	print table_line
	return
def process_poverty_by_sex_by_education(title_dict, data_dict):
        base_id="B17003"
        print banner
        print title_dict[base_id] + " (Poverty Rate)"
        print banner
        print "          Subtotal     <high_school    High_school     Associate     >=Bachelor"

	table_line = " Total:     "
	table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))+"            "
	for i in range(4,8):
		poverty = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+5)])
		population = int(data_dict[base_id][str(i+11)]) + int(data_dict[base_id][str(i+16)]) + poverty;
		table_line += two_digit_pc(str(poverty*100/population)) + "             ";
	print table_line
				
        table_line = "  Male:     "
	population = int(data_dict[base_id][str("3")]) + int(data_dict[base_id][str("14")])
	table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / population))+"            "
        for i in range(4,8):
		population = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+11)])
		table_line += two_digit_pc(str(int(data_dict[base_id][str(i)])*100 / population))+ "             "
        print table_line

	table_line = "Female:     "
        population = int(data_dict[base_id][str("8")]) + int(data_dict[base_id][str("19")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("8")])*100 / population))+"            "

        for i in range(4,8):
		population = int(data_dict[base_id][str(i+5)]) + int(data_dict[base_id][str(i+16)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+5)])*100 / population))+ "             "
        print table_line
        return
def process_poverty_by_sex_by_work_experience(title_dict, data_dict):
	base_id="B17004"
	print banner
	print title_dict[base_id] + " (Poverty Rate)"
	print banner
	print "         Subtotal     Full-time_job     Part-time_job     No_job"
	table_line = " Total:     "
        table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))+"            "
        for i in range(4,7):
                poverty = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+4)])
                population = int(data_dict[base_id][str(i+9)]) + int(data_dict[base_id][str(i+13)]) + poverty;
                table_line += two_digit_pc(str(poverty*100/population)) + "             ";
        print table_line

        table_line = "  Male:     "
        population = int(data_dict[base_id][str("3")]) + int(data_dict[base_id][str("12")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / population))+"            "
        for i in range(4,7):
                population = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+9)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i)])*100 / population))+ "             "
        print table_line

        table_line = "Female:     "
        population = int(data_dict[base_id][str("7")]) + int(data_dict[base_id][str("16")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("7")])*100 / population))+"            "

        for i in range(4,7):
                population = int(data_dict[base_id][str(i+4)]) + int(data_dict[base_id][str(i+9)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+4)])*100 / population))+ "             "
        print table_line
        return
def process_poverty_by_sex_by_employment_status(title_dict, data_dict):
	base_id="B17005"
	print banner
	print title_dict[base_id] + " (Poverty Rate)"
	print banner
	print "        Subtotal     In_labor_force     Employed     Unemployed     Not_in_labor_force"
	table_line = " Total:     "
        table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))+"            "
        for i in range(4,8):
                poverty = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+5)])
                population = int(data_dict[base_id][str(i+11)]) + int(data_dict[base_id][str(i+16)]) + poverty;
                table_line += two_digit_pc(str(poverty*100/population)) + "             ";
        print table_line

        table_line = "  Male:     "
        population = int(data_dict[base_id][str("3")]) + int(data_dict[base_id][str("14")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / population))+"            "
        for i in range(4,8):
                population = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+11)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i)])*100 / population))+ "             "
        print table_line

        table_line = "Female:     "
        population = int(data_dict[base_id][str("8")]) + int(data_dict[base_id][str("19")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("8")])*100 / population))+"            "

        for i in range(4,8):
                population = int(data_dict[base_id][str(i+5)]) + int(data_dict[base_id][str(i+11)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+5)])*100 / population))+ "             "
        print table_line
        return
def process_poverty_children_by_family_type_by_age(title_dict, data_dict):
	base_id="B17006"
	print banner
	print title_dict[base_id] + " (Poverty Rate)"
	print banner
	print "                    Subtotal        <5_years        5_years        6-17_years"
	table_line = "             Total:     "
        table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))+"            "
        for i in range(4,7):
                poverty = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+5)])
                population = int(data_dict[base_id][str(i+9)]) + int(data_dict[base_id][str(i+14)]) + poverty;
                table_line += two_digit_pc(str(poverty*100/population)) + "             ";
        print table_line

        table_line = "    Married-couple:     "
        population = int(data_dict[base_id][str("3")]) + int(data_dict[base_id][str("17")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / population))+"            "
        for i in range(4,7):
                population = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+14)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i)])*100 / population))+ "             "
        print table_line

        table_line = "  Male_householder:     "
        population = int(data_dict[base_id][str("8")]) + int(data_dict[base_id][str("22")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("8")])*100 / population))+"            "

        for i in range(4,7):
                population = int(data_dict[base_id][str(i+5)]) + int(data_dict[base_id][str(i+19)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+5)])*100 / population))+ "             "
        print table_line

	table_line = "Female_householder:     "
        population = int(data_dict[base_id][str("12")]) + int(data_dict[base_id][str("26")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("12")])*100 / population))+"            "

        for i in range(4,7):
                population = int(data_dict[base_id][str(i+9)]) + int(data_dict[base_id][str(i+23)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+9)])*100 / population))+ "             "
        print table_line

	table_line = "      Other_family:     "
        population = int(data_dict[base_id][str("7")]) + int(data_dict[base_id][str("21")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("7")])*100 / population))+"            "
	
	print table_line	
        return
def process_poverty_unrelated_by_sex_by_age(title_dict, data_dict):
	base_id="B17007"
        print banner
        print title_dict[base_id] + " (Poverty Rate)"
        print banner
        print "          Subtotal  15_yrs 16-17_yrs 18-24_yrs 25-34_yrs 35-44_yrs 45-54_yrs 55-64_yrs 65-74_yrs >75_yrs"

        table_line = " Total:     "
        table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))+"       "
        for i in range(4,13):
                poverty = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+10)])
                population = int(data_dict[base_id][str(i+21)]) + int(data_dict[base_id][str(i+31)]) + poverty;
                table_line += two_digit_pc(str(poverty*100/population)) + "       ";
        print table_line

        table_line = "  Male:     "
        population = int(data_dict[base_id][str("3")]) + int(data_dict[base_id][str("24")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / population))+"       "
        for i in range(4,13):
                population = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+21)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i)])*100 / population))+ "       "
        print table_line

        table_line = "Female:     "
        population = int(data_dict[base_id][str("13")]) + int(data_dict[base_id][str("34")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("13")])*100 / population))+"       "

        for i in range(4,13):
                population = int(data_dict[base_id][str(i+10)]) + int(data_dict[base_id][str(i+31)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+10)])*100 / population))+ "       "
        print table_line
        return
def income_deficit_unrelated_by_sex(title_dict, data_dict):
	base_id="B17008"
	print banner
	print title_dict[base_id] + " (Distribution)"	
	print banner
	print "           Deficit Percentage"

	table_line = "  Male:    "
	table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))
	print table_line

	table_line = "Female:    "
        table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / int(data_dict[base_id][str("1")])))
        print table_line
	return
def process_poverty_unrelated_by_work_by_householder(title_dict, data_dict):
	base_id="B17009"
	print banner
	print title_dict[base_id] + " (Poverty Rate)"
	print banner
	print "                     Subtotal  Nonfamily_householder  Other"
        table_line = "             Total:     "
        table_line += two_digit_pc(str(int(data_dict[base_id][str("2")])*100 / int(data_dict[base_id][str("1")])))+"            "
        for i in range(4,6):
                poverty = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+3)]) + int(data_dict[base_id][str(i+6)])
                population = int(data_dict[base_id][str(i+10)]) + int(data_dict[base_id][str(i+13)]) + int(data_dict[base_id][str(i+16)]) + poverty;
                table_line += two_digit_pc(str(poverty*100/population)) + "             ";
        print table_line

        table_line = "  Worked_full-time:     "
        population = int(data_dict[base_id][str("3")]) + int(data_dict[base_id][str("13")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("3")])*100 / population))+"            "
        for i in range(4,6):
                population = int(data_dict[base_id][str(i)]) + int(data_dict[base_id][str(i+11)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i)])*100 / population))+ "             "
        print table_line

        table_line = "  Worked_part-time:     "
        population = int(data_dict[base_id][str("6")]) + int(data_dict[base_id][str("16")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("6")])*100 / population))+"            "

        for i in range(4,6):
                population = int(data_dict[base_id][str(i+3)]) + int(data_dict[base_id][str(i+13)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+3)])*100 / population))+ "             "
        print table_line

	table_line = "      Did_not_work:     "
        population = int(data_dict[base_id][str("9")]) + int(data_dict[base_id][str("19")])
        table_line += two_digit_pc(str(int(data_dict[base_id][str("9")])*100 / population))+"            "

        for i in range(4,6):
                population = int(data_dict[base_id][str(i+6)]) + int(data_dict[base_id][str(i+16)])
                table_line += two_digit_pc(str(int(data_dict[base_id][str(i+6)])*100 / population))+ "             "
        print table_line
        return
def process_data(title_dict, data_dict):
	process_poverty_by_sex_by_age(title_dict, data_dict)
	print " "
	process_poverty_by_ratio_of_income(title_dict, data_dict)
	print " "
	process_poverty_by_sex_by_education(title_dict, data_dict)
	print " "
	process_poverty_by_sex_by_work_experience(title_dict, data_dict)	
	print " "
	process_poverty_by_sex_by_employment_status(title_dict, data_dict)
	print " "
	process_poverty_children_by_family_type_by_age(title_dict, data_dict)
	print " "
	process_poverty_unrelated_by_sex_by_age(title_dict, data_dict)
	print " "
	income_deficit_unrelated_by_sex(title_dict, data_dict)
	print " "
	process_poverty_unrelated_by_work_by_householder(title_dict, data_dict)
	print " "
	return
def read_data(dict):
	data = {}
	ans = open( "filterOUT.txt", "r" )
	for line in ans:
                line = line.strip()
                line = line.rstrip()
                line = line.lstrip()
                items = line.split("|")
                for i in range(len(items)):
                        items[i] = items[i].strip()
		current_id = items[2]
		current_index = items[3]
		items[5] = items[5].replace(",", "")
		current_data = items[5]

		if current_index == "1":
			data[current_id] = {}
		data[current_id][current_index] = current_data
	ans.close()
	return data


#defines variables
trueDir = False
output = ""
output2 = ""
"""
last1 = ""
last2 = ""
last3 = ""
last4 = ""
last5 = ""
"""
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


"""
tabs = 0 #Will's code
#####################################

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
"""

print("done")