import globals
from mapEgypt import mapEgypt
from mapUSA import mapUSA
class Help:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy =0
        self.me = 0

    def make_children(self , num , parent):

        adj = parent.adjacency
        ctrl = parent.control
        numList = parent.troopNum
        self.me = num
        if (num == 1):
            self.troops = parent.player1Available
            self.enemy = 2

        if (num == 2):
            self.troops = parent.player2Available
            self.enemy = 1



        l_deploy = []


        i = 0
        for x in ctrl:
            if(x != self.enemy and i != 0):
                child = self.deep_copy(parent)
                child.troopNum[i] = child.troopNum[i]+self.troops
                if(self.troops != 0):
                    child.control[i] = self.me

                if (num == 1):
                    child.player1Available -= self.troops

                if (num == 2):
                    child.player2Available -= self.troops

                l_deploy.append(child)
            i=i+1


        l_moved = []
        l_moved = l_deploy.copy() # hmmmmmmmmmmmm

        for map in l_deploy:
            i = 0
            for city in map.control:
                if (city == self.me and i != 0 and map.troopNum[i] > 1 ):

                    troops = map.troopNum[i]
                    for adj in map.adjacency[i]:
                        if(map.control[adj] != self.enemy and map.control[adj] != self.me):
                            child = self.deep_copy(map)
                            child.troopNum[adj] = troops - 1
                            child.troopNum[i] = 1
                            child.control[adj] = self.me
                            l_moved.append(child)

                        if(map.control[adj] != self.enemy and map.control[adj] == self.me):
                            child = self.deep_copy(map)
                            child.troopNum[adj] += troops - 1
                            child.troopNum[i] = 1
                            child.control[adj] = self.me
                            l_moved.append(child)
                i = i+1

        l_deploy.clear()

        l_attacked = []

        for map in l_moved:
            i = 0
            for city in map.control:
                if (city == self.me and i != 0 and map.troopNum[i] > 1):

                    troops = map.troopNum[i]
                    for adj in map.adjacency[i]:
                        if (map.control[adj] == self.enemy and troops > map.troopNum[adj]):
                            child = self.deep_copy(map)
                            child.troopNum[adj] = troops - 1
                            child.troopNum[i] = 1
                            child.control[adj] = self.me
                            l_attacked.append(child)

                        if (map.control[adj] != self.enemy and map.control[adj] != self.me):
                            child = self.deep_copy(map)
                            child.troopNum[adj] = troops - 1
                            child.troopNum[i] = 1
                            child.control[adj] = self.me
                            l_attacked.append(child)
                i = i + 1

        l_moved.clear()

        return l_attacked










    def deep_copy(self , map):
        copy = mapUSA()
        if(map.name == "egypt"):
            copy=mapEgypt()

        copy.troopNum = map.troopNum.copy()
        copy.control = map.control.copy()
        copy.player1Available = map.player1Available
        copy.player2Available = map.player2Available
        return copy

    def best_child(self, l_children):

        enemy = 9999999999999

        best = None
        for map in l_children:
            current = 0
            i=0
            mine =0
            for city in map.control:
                if (city == self.enemy and i != 0 ):
                    current += map.troopNum[i]
                if (city == self.me and i != 0 ):
                    mine +=1
                i = i + 1

            if(current-mine<enemy):
                enemy = current-mine
                best = map

        return best


    def calc_heurestic(self, child):

            i=0
            current = 0
            mine = 0
            for city in child.control:
                if (city == self.enemy and i != 0 ):
                 current += child.troopNum[i]
                if (city == self.me and i != 0 ):
                    mine +=1

                i = i + 1

            return current-mine


    def calc_heurestic2(self, child , me , enemy):

            i=0
            current = 0
            mine = 0
            for city in child.control:
                if (city == enemy and i != 0 ):
                 current += child.troopNum[i]
                if (city == me and i != 0 ):
                    mine +=1

                i = i + 1

            if(me == self.me):
                return (current-mine)*-1


            return current - mine










