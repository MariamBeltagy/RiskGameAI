import globals
from tkinter import *


class greedy:

    def move(self, num):
        adj = globals.map.adjacency
        ctrl = globals.map.control
        numList = globals.map.troopNum
        self.me = num
        ally = []  # ally index num
        attacker_index = []  # attacker index
        defender_index = []  # defender index
        h_of_attacks = []  # heuristic list
        special_case = []  # if all adj-->ally except for one.
        # if all possible attacks will lose we will choose a movement between 2 allys
        # that will result the max number of troops
        max_ally = []  # contains the max move for each ally that have an enemy adj
        max_ally_send = []
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

        i = 0
        while (i < m):
            if (ctrl[i] == self.me):
                ally.append(i)
            i += 1

        i = 0
        while (range(0, len(ally))):
            a = []  # diff between num of troops of attacker and adj enemy
            b = []  # total num of troops after moving from the attacker to the adj ally
            a_index = []
            b_index = []
            j = 0
            while (range(0, len(adj[i][j]))):
                if (ctrl[adj[i][j]] != self.me):
                    a.append(numList[ally[i]] - numList[adj[i][j]])
                    a_index.append(j)
                else:
                    b.append(numList[adj[i][j]])
                    b_index.append(j)
                j += 1
            if (a != None):
                h_of_attacks.append(max(a))
                attacker_index.append(i)
                defender_index.append(a_index[a.index(max(a))])
                if (len(a) == 1):
                    special_case.append(1)
                else:
                    special_case.append(0)
                if (b != None):
                    max_ally.append(max(b))
                    max_ally_send.append(b_index[b.index(max(b))])

                else:
                    max_ally.append(None)

            i += 1
        if (max(h_of_attacks > 0)):
            index = h_of_attacks.index(max(h_of_attacks))
            attacker = attacker_index[index]
            defender = defender_index[index]
            if (special_case[index] == 1):
                numList[defender] = numList[defender] - numList[attacker]
                numList[attacker] = 1
                ctrl[defender] = self.me
            else:
                if (numList[attacker] / 2 >= numList[defender]):
                    numList[defender] = numList[defender] - numList[attacker] / 2
                    numList[attacker] = numList[attacker] / 2
                    ctrl[defender] = self.me
                else:
                    numList[defender] = 1
                    numList[attacker] -= (numList[defender] + 1)
                    ctrl[defender] = self.me
        else:
            i = 0
            new_h = []
            while (range(0, len(max_ally))):
                if (max_ally != None):
                    new_h.append((max_ally[i] - 1 + h_of_attacks[i]))
                i += 1
            if (max(new_h) > 0):
                receiver = attacker_index[new_h.index(max(new_h))]
                sender=max_ally_send[new_h.index(max(new_h))]
                numList[receiver] += max_ally[new_h.index(max(new_h))] - 1
                numList[sender] = 1
