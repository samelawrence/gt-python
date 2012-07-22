# Filming Code
# Sam Lawrence
# Solace Collestan
# samlawrence@gatech.edu
# scollestan@gatech.edu
# We worked on this part alone.

from myro import *


"""Function that loops for 60 seconds and records like a movie. Exports a .gif
and .jpg's of each frame for future manipulation in the editing code. Returns
the picture list for the performance code or editing code."""

def filmLoop():
    pictureList=[]
    counter=1
    while timeRemaining(60):        #Begin Filming
        p=takePicture()
        pictureList.append(copyPicture(p))
        print "Filming please wait..."
    for item in pictureList:        #Export jpg's.
        savePicture(item,"intro"+str(counter)+".jpg")
        counter+=1
    savePicture(pictureList,"chase.gif")    #Export animated gif.
    return pictureList
