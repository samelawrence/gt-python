# Sam Lawrence
# Solace Collestan
# 8/26/09
# samlawrence@gatech.edu
# scollestan@gatech.ed
# We worked on this assignment together.

from math import *

# Function for converting kilograms to stones:
def mass(kg):
    stones = kg * (0.157)
    return(stones)

# Function for converting liters into US pints using an input rather than a parameter:

def volume(liters):
    USpints = liters * 2.11
    print ("There are %.2f pints in %.2f liters." %(USpints,liters))

#Function for converting monkeys to hockey pucks using an input rather than an parameter:

def monkeys(monkeys):
    hockeyPucks = monkeys * 37.62533333333
    print ("There are %.4f Hockey Pucks in %.4f monkeys." %(hockeyPucks,monkeys))

# Function for a tip calculator: Our calculator calculates tip rounded to next dollar.

def tipCalculator():
    subTotal = raw_input("What was the bill before tax and gratuity? ")
    subTotal = float(subTotal)
    tip = raw_input("What percentage tip would you like to leave? ")
    tax = subTotal * 0.078
    tip = float(tip)
    tip = (subTotal + tax) * (tip/100.0)
    tip=ceil(tip) #Rounds tip up to the next dollar.
    total = (subTotal + tax + tip)
    print ("tax = $%.2f" %tax)
    print ("tip = $%.2f" %tip)
    print ("total = $%.2f" %total)
