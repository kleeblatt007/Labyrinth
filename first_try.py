import numpy as np
import pprint as pp
import random

#1: Wand
#0: keine Wand


class Spieler:

    position = ()
    def __init__(self, position= (0,0)):
        self.position = position
        self.x = position[0]
        self.y = position[1]

    def checkMoves(self, lab):
        availableMoves = []

        if lab[self.y+1][self.x] == 0:
            availableMoves.append("down")
        if lab[self.y-1][self.x] == 0:
            availableMoves.append("up")
        if lab[self.y][self.x-1] == 0:
            availableMoves.append("left")
        if lab[self.y][self.x+1] == 0:
            availableMoves.append("right")

        return availableMoves

    def move(self, direction):
        if direction == "up":
            self.y -= 1
        elif direction == "down":
            self.y += 1
        elif direction == "left":
            self.x += 1
        elif direction == "right":
            self.x -= 1

        self.position = (self.x,self.y)

def generateLab(size):
    a = [[0 for i in range(size)]for x in range(size)]

    for i in range(size):
        for x in range(size):
            if i == 0 or i == size-1 or x == 0 or x == size-1:
                a[i][x]=1
            elif i < size-2 and x<size-2:
                if a[i-1][x-1]==1 and a[i+1][x+1]==1:
                    a[i][x]=0
            else:
                a[i][x] = random.randint(0, 1)

    a[size-1][size-2]=0
    return a



lab = generateLab(15)
player1 = Spieler()

pp.pprint(lab)
