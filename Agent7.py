import globals
from Help import Help


class Agent7:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy = 0
        self.me = 0
        self.cost = 0

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

        helper = Help()

        parent = globals.map

        best_score = 99999999999
        self.cost += 1

        while (1):
            children = helper.make_children(num, parent)
            if children.__len__() != 0:
                best = helper.best_child(children)
                score = helper.calc_heurestic(best) + self.cost
            else:
                break

            if (best_score <= score):
                break
            best_score = score

            parent = best

            children.clear()

        globals.map.troopNum = parent.troopNum.copy()
        globals.map.adjacency = parent.adjacency.copy()
        globals.map.control = parent.control.copy()
        globals.map.player1Available = parent.player1Available
        globals.map.player2Available = parent.player2Available
