# Solace Collestan
# Sam Lawrence
# October 19, 2009
# scollestan@gatech.edu
# samlawrence@gatech.edu
# We worked on this assignment with Courtney Price, Farzon Lotfi and Joseph Rao IV.

from myro import *

init('com4')

def countYellows(pic):
    countYellowPix=0
    for pixel in getPixels(pic):
        if getRed(pixel)>=190  and getGreen(pixel)>=140 and getBlue(pixel)<=135:
            countYellowPix+=1
    return countYellowPix
            
def celebrate():
    speak("I win! We found it!")
    for i in range(0,2):
        beep(.5,680)
        turnLeft(1,1)
    

def findYellow():
    while True:
        p=takePicture()
        yellowPixels=countYellows(p)
        print yellowPixels
        show(p)

        if yellowPixels>=2500 and getObstacle("center")>900:
            celebrate()
            stop()
            return
            
        elif yellowPixels>=2500:
            forward(.5,1)
                      
        else:
            turnRight(.5,.6)

findYellow()
