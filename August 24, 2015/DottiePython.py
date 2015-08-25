import math

def findDottie(numIn):
    guess1 = math.fabs(numIn)
    guess2 = math.fabs(math.cos(numIn))
    while(math.fabs(guess1 - guess2) > 0.00001):
        guess1 = guess2
        guess2 = math.fabs(math.cos(guess1))
    return guess2

print(findDottie(15))
