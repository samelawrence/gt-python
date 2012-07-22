# Acting Code
# Sam Lawrence
# Solace Collestan
# samlawrence@gatech.edu
# scollestan@gatech.edu
# We worked on this with Farzon Lotfi and Joeseph Rao IV.

from myro import *

"""Opening"""

def opening():
    gamepad()

"""Bond Intro"""

def intro():
    forward(.3,3.5)
    wait(1)
    turnLeft(.6,.3)
    setLEDFront(1)
    wait(2)
    setLEDFront(0)
