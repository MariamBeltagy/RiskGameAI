import globals
from tkinter import *
class Agent1:
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
        minenemy = None
        myter = 0
        enemy = []
        ally = []
        i = 0
        if (globals.map == "egypt"):
            while (i < 28):
                if (ctrl[i] == self.me):
                    myter += 1
                    ally.append(i)
                    if (min > numList[i] or min == None):
                        i_min = i
                        min = numList[i]
                elif (ctrl[i] != 0):
                    enemy.append(i)
                    if (minenemy > numList[i] or minenemy == None):
                        minenemy = numList[i]
                        minenemyindex = i
            i+=1
        else:
            while (i < 51):
                if (ctrl[i] == self.me):
                    myter += 1
                    ally.append(i)
                    if (min > numList[i] or min == None):
                        i_min = i
                        min = numList[i]
                elif (ctrl[i] != 0):
                    enemy.append(i)
                    if (minenemy > numList[i] or minenemy == None):
                        minenemy = numList[i]
                        minenemyindex = i
            i+=1

        newtroops = int(myter / 3)
        if (newtroops < 3):
            newtroops = 3

        numList[i_min] += newtroops
        i = ally.__len__()-1
        attacker = None
        while (i >= 0):
            if (adj[minenemyindex].__contains__(ally[i])):
                if (numList[ally[i]] > numList[minenemyindex]):
                    if (attacker == None or numList[attacker] < numList[ally[i]]):
                        attacker = ally[i]
            i -= 1

        if (attacker != None):
            if (numList[attacker] > numList[minenemyindex]):
                numList[minenemyindex] = numList[attacker] - numList[minenemyindex]
                ctrl[minenemyindex] = self.me
                numList[attacker] = 1