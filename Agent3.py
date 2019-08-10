import globals
from tkinter import *
class Agent3:
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


        max = None
        enemy = []
        maxenemy = None
        ally = []
        myter = 0
        i = 0
        if (globals.map == "egypt"):
            while (i < 28):
                if (ctrl[i] == self.me):
                    myter += 1
                    ally.append(i)
                    if (max < numList[i] or max == None):
                        i_max = i
                        max = numList[i]
                elif (ctrl[i] != 0):
                    enemy.append(i)
                i += 1
        else:
            while (i < 51):
                if (ctrl[i] == self.me):
                    myter += 1
                    ally.append(i)
                    if (max < numList[i] or max == None):
                        i_max = i
                        max = numList[i]
                elif (ctrl[i] != 0):
                    enemy.append(i)
                i += 1

        newtroops = int(myter / 3)
        if (newtroops < 3):
            newtroops = 3

        numList[i_max] += newtroops

        i = enemy.__len__()-1
        while (i >= 0):
            j = len(adj[enemy[i]])
            while (j >= 0):
                k = ally.__len__()-1
                while (k >= 0):
                    if (ally[k] == adj[enemy[i]][j]):
                        if (numList[ ally[k] ] > 1):
                            if (maxenemy == None or maxenemy < numList[enemy[i]]):
                                maxenemy = numList[enemy[i]]
                                attacker = ally[k]
                                defender = enemy[i]
                            elif (maxenemy == numList[enemy[i]]):
                                if (numList[attacker] < numList[ally[k]]):
                                    attacker = ally[k]
                                    defender = enemy[i]

                    k -= 1

                j -= 1
            i -= 1
        if (maxenemy != None):
            if (numList[attacker] > numList[defender]):
                numList[defender] = numList[attacker] - numList[defender]
                ctrl[defender] = self.me
                numList[attacker] = 1
            elif (numList[attacker] < numList[defender]):
                numList[defender] = numList[defender] - numList[attacker]
                numList[attacker] = 1
            else:
                numList[attacker] = 1
                numList[defender] = 0
                ctrl[defender] = 0
