# Filming Code
# Sam Lawrence
# Solace Collestan
# samlawrence@gatech.edu
# scollestan@gatech.edu
# We worked on this part alone.


from myro import *
from random import *

#Take a list of pictures and saves each one as a .jpg.

def picSaver(listOfPictures):
    counter=1
    for item in listOfPictures:
        savePicture(item,"pic"+str(counter)+".jpg")
        counter+=1
        

#Begin Seeing Red
"""Takes a picture object in as a parameter(optional use takePicture() function)
and saves a .gif transforming it to a red tint through a top-down wipe to smiulate
the effect from the James Bond Intro. Then returns the picture list
for optional further manipulation or debugging."""

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

"""Should be applied to one frame, as it outputs more frames."""

#Begin Cross Fade
"""Takes in two picture objects as parameters (the loadPicture()[for file paths],
and takePicture() functions are useful) and wipes from the first picture to the
second picture from right to left. Shows progress, returns picture list and
saves an animated gif."""
def crossFade(scene1,scene2):
    #show(scene1)
    pictureList=[scene1]
    #Traverse the pixels.
    for x in range(getWidth(scene1))[::-1]:
        for y in range(getHeight(scene1))[::-1]:
            scene1=copyPicture(scene1) #Copy the picture for making animated gif.
            pixel1=getPixel(scene1,x,y) #Get scene1's pixel.
            pixel2=getPixel(scene2,x,y) #Get scene2's pixel
            setPixel(scene1,x,y,getColor(pixel2)) #Set to scene2's pixel.
        #repaint(scene1)
        pictureList.append(scene1) #For animated gif.
    savePicture(pictureList,'crossFade.gif') #Saves animated gif.
    return pictureList

"""Cross Fade is best applied the last frame of one scene and the first frame of
the next scene."""

#Begin Dissolve
"""Disolves the image to black. Should be applied to one frame. Returns the
picture list."""
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
        
        if len(pictureList)>125:
            for x in range(getWidth(picture)):
               for y in range(getHeight(picture)):
                   pixel=getPixel(picture,x,y)
                   setRed(pixel,0)
                   setGreen(pixel,0)
                   setBlue(pixel,0)
            pictureList.append(picture)
            repaint(picture)
            traverse=False
            print "DONE!"
        elif counter>1800:
            pictureList.append(picture)
            repaint(picture)
            counter=0
            print "DISSOLVING!"
    savePicture(pictureList,'dissolve.gif')
    return pictureList
