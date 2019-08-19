import globals
from tkinter import *
from Help import Help
class Help2:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy =0
        self.me = 0
        self.cost = 0

    def make_children(self , num  , parents):

        adj = parents.adjacency
        ctrl = parents.control
        numList = parents.troopNum
        self.me = num
        if (num == 1):
            self.troops = parents.player1Available
            self.enemy = 2

        if (num == 2):
            self.troops = parents.player2Available
            self.enemy = 1

        helper = Help()

        parent = parents




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

            if(helper.calc_heurestic(parent) <= -50 or number >= 21):
                break

            number+=1


        l_best = []
        q = 0
        while(q<best_children.__len__() and q <2):

         l_best.append(helper.deep_copy(helper.best_child(best_children)))
         best_children.remove(helper.best_child(best_children))
         q+=1

        return l_best






