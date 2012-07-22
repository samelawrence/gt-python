# hw7
# Solace Collestan
# Sam Lawrence
# scollestan@gatech.edu
# samlawrence@gatech.edu
# We worked on this assignment with Joseph Rao IV and Farzon Lotfi.

from myro import *
from random import *
#init()


#Begin Seeing Red
"""Takes a picture object in as a parameter(optional use takePicture() function)
and saves a .gif transforming it to a red tint through a top-down wipe to smiulate
the effect from the James Bond Intro. Then returns the picture list
for optional further manipulation or debugging. We feel that because this is a transition
effect it should be worth 5-10 points greater than a basic seeing red."""

def seeingRed(picture):
    show(picture,'Seeing Red!')
    pictureList=[picture]
    #Traverse the pixels.
    for y in range(getHeight(picture)):
        for x in range(getWidth(picture)):
            picture=copyPicture(picture) #Copy the picture for making animated gif.
            pixel=getPixel(picture,x,y)
            #Reduce blue and green values in the picture in order to tint red.
            setBlue(pixel,(getBlue(pixel)*.2))
            setGreen(pixel,(getGreen(pixel)*.2))
        show(picture, 'Seeing Red!')
        pictureList.append(picture) #For animated gif.
    savePicture(pictureList,'seeingRed.gif') #Saves animated gif.
    return pictureList

#Begin Dolly Shot
"""Takes the number of shots in as a parameter, causes the scribbler to move in order
to execute a dolly shot, saves the dolly shot as an animated gif, and then returns
the picture list for optional further manipulation or debugging."""

def dollyShot(shotCount):
    pictureList=[]
    while len(pictureList)<(shotCount):
        picture=takePicture()
        picture=copyPicture(picture)
        turnRight(.7, .5)
        forward (.7, .5)
        turnLeft(.7, .5)
        pictureList.append(picture)
    stop()
    savePicture(pictureList, 'dollyShot.gif')
    return pictureList

#Begin Robot Zoom
"""Takes a picture saves it into a list and then moves forward and repeats the process.
Outputs an animated gif, and returns the picture list for optional further manipulation
and/or debugging."""

def robotZoom():
        pictureList=[]
	while getObstacle("center")<500:
		picture = takePicture()
		picture=copyPicture(picture)
		show(picture)
		pictureList.append(picture)
		forward (1, .5)
	savePicture(pictureList, "robotZoom.gif")
	return pictureList


#Begin Rotating Shot
"""Takes a rotating shot. The number of shots is equal to the parameter passed in as
an integer. Shows pictures as it takes them, saves an animated gif and returns
the picture list for optional debugging or further manipulation."""

"""While this program is at the same difficulty level of 360 view (a 20 point assignment),
we feel that since this program completes and even extends the functionality of that program's
purpose, we should be awarded at least 30 points. This new program allows the cameraman
to create a shot around a rotating point for any angle he chooses, be it a 360 panorama,
or just a quarter-turn."""
def rotatingShot(count):
	pictureList = []
	while count>0:
                wait(.1)
		picture = takePicture()
		picture = copyPicture(picture)
		pictureList.append(picture)
                show (picture)
		turnRight(.25, .25)
		count-=1
	savePicture(pictureList, "rotatingShot.gif")
	return (pictureList)

#Begin Fade
"""Reduces color values of pixels in the picture over 11 iterations. In a twelth
iteration the pixel values are reduced to zero to complete the fade.
Note: This code takes a long time to execute and thus the effect is not very apparent
in the myro picture window. Please see accompaning gif file or create your own
using the code see the effect."""

def fade(picture):
    show(picture)
    pictureList=[picture]
    for iteration in range(11):
        for x in range(getWidth(picture)):
            for y in range(getHeight(picture)):
                picture=copyPicture(picture) #Copy the picture for making animated gif.
                pixel=getPixel(picture,x,y)
                #Reduce color values of to fade.
                setRed(pixel,(getRed(pixel)*.9))
                setBlue(pixel,(getBlue(pixel)*.9))
                setGreen(pixel,(getGreen(pixel)*.9))
        repaint(picture)
        pictureList.append(picture)
    #Finalize the picture with black.
    for x in range(getWidth(picture)):
        for y in range(getHeight(picture)):
            picture=copyPicture(picture) #Copy the picture for making animated gif.
            pixel=getPixel(picture,x,y)
            #Reduce color values of picture to black.
            setRed(pixel,(0))
            setBlue(pixel,(0))
            setGreen(pixel,(0))
    repaint(picture)
    pictureList.append(picture) #For animated gif.
    savePicture(pictureList,'fade.gif') #Saves animated gif.
    return pictureList

#Begin Cross Fade
"""Takes in two picture objects as parameters (the loadPicture()[for file paths],
and takePicture() functions are useful) and wipes from the first picture to the
second picture from right to left. Shows progress, returns picture list and
saves an animated gif. We feel that this code should be worth the same amount as a
crossfade because it is just as complicated."""
def crossFade(scene1,scene2):
    show(scene1)
    pictureList=[scene1]
    #Traverse the pixels.
    for x in range(getWidth(scene1))[::-1]:
        for y in range(getHeight(scene1))[::-1]:
            scene1=copyPicture(scene1) #Copy the picture for making animated gif.
            pixel1=getPixel(scene1,x,y) #Get scene1's pixel.
            pixel2=getPixel(scene2,x,y) #Get scene2's pixel
            setPixel(scene1,x,y,getColor(pixel2)) #Set to scene2's pixel.
        repaint(scene1)
        pictureList.append(scene1) #For animated gif.
    savePicture(pictureList,'crossFade.gif') #Saves animated gif.
    return pictureList

#Begin Dissolve
"""Disolves the image to black. We this this code is worth 35 and 50 points."""
def dissolve(picture):
    pixelList=[]
    for x in range(getWidth(picture)):
        for y in range(getHeight(picture)):
            pixelList.append((x,y))
    shuffle(pixelList)
    
    show(picture)
    pictureList=[picture]
    counter=0
    traverse=True
    while traverse:
        picture=copyPicture(picture)
        pixel=choice(pixelList)
        pixel=getPixel(picture,pixel[0],pixel[1])
        setRed(pixel,0)
        setGreen(pixel,0)
        setBlue(pixel,0)
        counter+=1
        
        if len(pictureList)>500:
            for x in range(getWidth(picture)):
               for y in range(getHeight(picture)):
                   pixel=getPixel(picture,x,y)
                   setRed(pixel,0)
                   setGreen(pixel,0)
                   setBlue(pixel,0)
            pictureList.append(picture)
            repaint(picture)
            traverse=False
        elif counter>1300:
            pictureList.append(picture)
            repaint(picture)
            counter=0
    savePicture(pictureList,'dissolve.gif')
    return pictureList

