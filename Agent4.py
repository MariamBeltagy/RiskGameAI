import globals
from tkinter import *
class Agent4:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy =0
        self.me = 0

    def move(self , num , infoText , listL):
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

        minCity = 0
        mminTroops = 99999
        i = 0
        for num in numList:
            if num < mminTroops and ctrl[i] != self.enemy and i != 0:
                minCity = i
                mminTroops=num
            i=i+1

        ctrl[minCity] = self.me
        numList[minCity] = numList[minCity] + self.troops

        if (self.me == 1):
            globals.map.player1Available = 0

        if (self.me == 2):
            globals.map.player2Available = 0

        attack = 0
        attacked = 0
        minEnemyArmy = 999999
        i = 0
        for city in adj:
            if ctrl[i] == self.me and i != 0:
                for adjs in city:

                    if numList[i] > numList[adjs] and minEnemyArmy > numList[adjs] and ctrl[adjs] != self.me and numList[i] > 1:

                        attack = i
                        attacked = adjs
                        minEnemyArmy = numList[adjs]

            i = i + 1


        if (attack != 0 and attacked != 0 and numList[attack] > 1):
            numList[attacked] = numList[attack] - 1
            numList[attack] = 1
            ctrl[attacked] = self.me
