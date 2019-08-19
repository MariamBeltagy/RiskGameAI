import globals
from tkinter import *
from Help import Help
class Agent6:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy =0
        self.me = 0
        self.cost = 0

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

        helper = Help()

        parent = globals.map

        best_score = 99999999999
        self.cost+=1
        best_children = []
        number = 0
        children = []
        visited = []
        children.append(parent)
        while (1):
            children.remove(parent)
            current_children = helper.make_children(num, parent)

            for mapA in current_children:
                for mapB in visited :
                    if(mapA.control == mapB.control and mapA.troopNum == mapB.troopNum  ):
                        current_children.remove(mapA)
                        break


            if(current_children.__len__() != 0):
                visited = visited + current_children.copy()
                children = children + current_children.copy()



            if children.__len__() !=0 :

                best = helper.best_child(children)
                best_children.append(helper.deep_copy(best))
                score = helper.calc_heurestic(best) + self.cost
            else:
                break

            best_score = score
            parent = best

            if(helper.calc_heurestic(parent) <= -50 or number >= 99):
                break

            number+=1



        parent = helper.best_child(best_children)
        if (parent != None):
                globals.map.troopNum = parent.troopNum.copy()
                globals.map.adjacency = parent.adjacency.copy()
                globals.map.control = parent.control.copy()
                globals.map.player1Available = parent.player1Available
                globals.map.player2Available = parent.player2Available



