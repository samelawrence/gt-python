# Sam Lawrence
# Solace Collestan
# 9/11/09
# samlawrence@gatech.edu
# scollestan@gatech.edu
# We worked on this assignment together.

def dec2binary(decNum):
    binary=""
    while decNum>0:
        
        binary=str(decNum%2)+binary
        decNum = decNum/2
       
    return binary

def binary2dec(binString):
    decimal=0
    power=len(binString)-1
    for number in binString:
        digit=int(number)
        decimal=decimal+(digit*2**power)
        power=power-1
    return decimal
