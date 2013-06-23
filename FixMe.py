# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>
# <codecell>

def test(x, y, z):
    
    #First test for a number
    try:
        float(x) ** 1/2
        onetest = 3
        boolone = True
    except ValueError:
        onetest = 2
        boolone = False
    #second test for a number
    try:
        float(y) ** 1/2
        twotest = onetest
        booltwo = True
    except ValueError:
        twotest = onetest - 1
        booltwo = False
    #third test for a number
    try:
        float(z) ** 1/2
        threetest = twotest
        boolthree = True
    except ValueError:
        threetest = twotest - 1
        boolthree = False
    #Return a value for the test
    if threetest == 2 and boolone == True:
        return 1
        print "1"
    elif threetest == 2 and booltwo == True:
        return 2
        print "2"
    elif threetest == 2 and boolthree == True:
        return 3
        print "3"
    else:
        return 4
        print "error"

# <codecell>

#solve for the first leg if it is a letter
def solveone(one, itwo, ithree):
    two = float(itwo)
    three = float(ithree)
    twosquare = two ** 2
    threesquare = three ** 2
    onesquare = threesquare - twosquare
    onefinal = onesquare ** 1/2
    result = "The final product for " + one + " is " + str(onefinal)
    return result
    print "one result"
#solve for the second leg if it is a letter
def solvetwo(ione2, two2, ithree2):
    one2 = float(ione2)
    three2 = float(ithree2)
    one2square = one2 ** 2
    three2square = three2 ** 2
    two2square = three2square - one2square
    two2final = two2square ** 1/2
    result2 = "The final product for " + two2 + " is " + str(two2final)
    return result2
    print "two result"
#solve for the third leg if it is a letter
def solvethree(ione3, itwo3, three3):
    one3 = float(ione3)
    two3 = float(itwo3)
    one3square = one3 ** 2
    two3square = two3 ** 2
    three3square = one3square + two3square
    three3final = three3square ** 1/2
    result3 = "The final product for " + three3 + " is " + str(three3final)
    return result3
    print "three result"

# <codecell>

print "Welcome to Pothag v1.0 [By: Will]"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# <codecell>

while True:
    first = str(raw_input("First leg ('x' if value unknown): "))
    second = str(raw_input("Second leg ('x' if value unknown): "))
    third = str(raw_input("Hypotenus ('x' if value unknown): "))
    tresult = float(test(first, second, third))
    if tresult == 1:
        print solveone(first, second, third)
    elif tresult == 2:
        print solvetwo(first, second, third)
    elif tresult == 3:
        print solvethree(first, second, third)
    elif tresult == 4:
        print "Error: [Please ensure two of the values are raw numbers]"
    else:
        print "ERROR"
    raw_input("Press enter to continue")

# <codecell>