import globals


class Agent3:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy = 0
        self.me = 0

    def move(self, num, infoText, listL):

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

        maxCity = 0
        mmaxTroops = -1
        i = 0
        for num in numList:
            if num > mmaxTroops and ctrl[i] != self.enemy and i != 0:
                maxCity = i
                mmaxTroops = num
            i = i + 1

        ctrl[maxCity] = self.me
        numList[maxCity] = numList[maxCity] + self.troops

        if (self.me == 1):
            globals.map.player1Available = 0

        if (self.me == 2):
            globals.map.player2Available = 0

        attack = 0
        attacked = 0
        maxEnemyArmy = -1
        i = 0

        while (1):
            i = 0
            maxEnemyArmy = -1
            for city in adj:
                if ctrl[i] == self.me and i != 0:
                    for adjs in city:
                        if numList[i] > numList[adjs] and maxEnemyArmy < numList[adjs] and ctrl[adjs] == self.enemy:
                            attack = i
                            attacked = adjs
                            maxEnemyArmy = numList[adjs]
                i = i + 1

            if (attack != 0 and attacked != 0 and numList[attack] > 1):

                numList[attacked] = numList[attack] - 1
                numList[attack] = 1
                ctrl[attacked] = self.me

            elif ((attack == 0 and attacked == 0) or numList[attack] < 2):
                break
