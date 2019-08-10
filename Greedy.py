import globals
from tkinter import *


class greedy:
    def move(self, num):
        adj = globals.map.adjacency
        ctrl = globals.map.control
        numList = globals.map.troopNum
        self.me = num
        ally = []
        allynum = []
        i = 0
        if (self.me == 1):
            self.troops = globals.map.player1Available
            self.enemy = 2

        if (self.me == 2):
            self.troops = globals.map.player2Available
            self.enemy = 1

        if (globals.map == "egypt"):
            m = 28
        else:
            m = 51

        while (i < m):
            if (ctrl[i] == self.me):
                ally.append(i)
                allynum.append(numList[i])
            i += 1
        fro = ally[allynum.index(max(allynum))]

        j = len(adj[fro]) - 1
        ally = []
        enemy = []
        while (j >= 0):
            if (ctrl[adj[fro][j]] == self.me):
                ally.append(adj[fro][j])
            else:
                enemy.append(adj[fro][j])
            j -= 1

        lene = len(enemy)
        if (lene != 0):
            step = []
            k = 0
            while (range(0, lene)):
                step.append(numList[fro] - numList[enemy[k]] - 1)
                k += 1
            to = enemy[step.index(max(step))]
            if (numList[to] > numList[fro] - 1):
                numList[to] -= numList[fro] - 1
                numList[fro] = 1
            elif (numList[to] == numList[fro] - 1):
                numList[to] = 0
                numList[fro] = 1
                ctrl[to] = 0
            else:
                numList[to] = numList[fro] - numList[to] - 1
                numList[fro] = 1
                ctrl[to] = self.me

        else:
            lene = len(ally)
            step = []
            k = 0
            while (range(0, lene)):
                step.append(numList[fro] + numList[enemy[k]] - 1)
                k += 1

            to = ally[step.index(max(step))]
            numList[to] += numList[fro] - 1
            numList[fro] = 1