import globals
from tkinter import *
class Agent2:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy =0
        self.me = 0

    def move(self , num , infoText):
        adj = globals.map.adjacency
        ctrl = globals.map.control
        numList = globals.map.troopNum
        self.me = num
        if (num == 1):
            self.troops = globals.map.player1Available
            self.enemy = 2

        if (num == 2):
            self.troops = globals.map.player2Available
            self.enemy = 1
        min = None
        myter = 0
        i = 0
        if (globals.map == "egypt"):
            while (i < 28):
                if (ctrl[i] == self.me):
                    myter += 1
                    if (min > numList[i] or min == None):
                        i_min = i
                        min = numList[i]
            i+=1
        else:
            while (i < 51):
                if (ctrl[i] == self.me):
                    myter += 1
                    if (min > numList[i] or min == None):
                        i_min = i
                        min = numList[i]
            i+=1

        newtroops = int(myter / 3)
        if (newtroops < 3):
            newtroops = 3

        numList[i_min] += newtroops
