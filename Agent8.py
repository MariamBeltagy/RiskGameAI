import globals
from Help import Help
from Help2 import Help2


class Agent8:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy = 0
        self.me = 0

    def move(self, num, infoText, listL):

        self.me = num
        if (num == 1):
            self.troops = globals.map.player1Available
            self.enemy = 2

        if (num == 2):
            self.troops = globals.map.player2Available
            self.enemy = 1

        current = self.minimax(self.me, self.enemy, 4, globals.map, -9999, 9999)
        globals.map.control = current.control.copy()
        globals.map.troopNum = current.troopNum.copy()
        globals.map.player1Available = current.player1Available
        globals.map.player2Available = current.player2Available

    def minimax(self, me, enemy, depth, state, alpha, beta):
        helper = Help()
        helper.enemy = self.enemy
        helper.me = self.me

        if (depth == 0 or helper.calc_heurestic2(state, me, enemy) >= 50):
            score = helper.calc_heurestic2(state, me, enemy)
            return score

        if (me == self.me):

            num = me
            chosen_map = None
            max = -9999
            helper2 = Help2()
            children = helper2.make_children(self.me, state)

            for child in children:
                if (me == 1):
                    num = child.control.count(1)

                    num = int(num / 3)

                    if (num < 3):
                        num = 3
                    child.player1Available += num

                else:
                    num = child.control.count(2)
                    num = int(num / 3)
                    if (num < 3):
                        num = 3
                    child.player2Available += num

                next = self.minimax(self.enemy, self.me, depth - 1, child, alpha, beta)

                if (next > max):
                    max = next
                    child.player1Available -= num
                    chosen_map = helper.deep_copy(child)

                if (next > alpha):
                    alpha = next

                if (alpha >= beta):
                    break

            if (children.__len__() == 0):
                chosen_map = helper.deep_copy(state)
                min = helper.calc_heurestic2(state, me, enemy)

            if (depth == 4):
                return chosen_map

            return max

        if (me == self.enemy):

            num = me
            chosen_map = None
            min = 999999
            helper2 = Help2()
            children = helper2.make_children(self.enemy, state)

            for child in children:
                if (me == 1):
                    num = child.control.count(1)

                    num = int(num / 3)

                    if (num < 3):
                        num = 3
                    child.player1Available += num

                else:
                    num = child.control.count(2)
                    num = int(num / 3)
                    if (num < 3):
                        num = 3
                    child.player2Available += num

                next = self.minimax(self.me, self.enemy, depth - 1, child, alpha, beta)

                if (next < min):
                    min = next
                    child.player1Available -= num
                    chosen_map = helper.deep_copy(child)

                if (next < beta):
                    beta = next

                if (alpha >= beta):
                    break

            if (children.__len__() == 0):
                chosen_map = helper.deep_copy(state)
                min = helper.calc_heurestic2(state, me, enemy)

            if (depth == 4):
                return chosen_map
            return min
