import random
import os

def clearScreen():
    os.system('cls')

def randomCell():
    row = random.randrange(10)
    column = random.randrange(10)
    return [row, column]

def randomDirection():
    return random.randrange(2)