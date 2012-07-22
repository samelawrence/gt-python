# Solace Collestan
# Sam Lawrence
# September 02, 2009
# scollestan@gatech.edu
# samlawrence@gatech.edu
# We worked on this program together.

def coffee():
    cupsCoffee = int(raw_input("How many cups of coffee did you have today?: "))
    hoursSleep = int(raw_input("How many hours of sleep did you get last night?: "))
    #Calculate Score
    score=3*cupsCoffee+hoursSleep

    if score>=12:
        return "super hyper"

    elif score>=6 and score<12:
        return "mellow"

    elif score<6:
        return "sluggish"

def typeOfDay():
    print("The weather was favorable today (enter YES for true, NO for false):")
    day=raw_input()
    if day=="YES":
        weather=True
    elif day=="NO":
        weather=False

    print("I had a good time with my friends today (enter YES for true, NO for false):")
    friends=raw_input()
    if friends=="YES":
        time=True
    elif friends=="NO":
        time=False

    if weather==True and time==True:
        return "spectacular"
    elif weather==False and time==True:
        return "decent"
    elif weather==True and time==False:
        return "decent"
    elif weather==False and time==False:
        return "crummy"


def main():
    java=coffee()
    party=typeOfDay()

    print("You completed a " + party + " day in a " + java + " manner!!")
