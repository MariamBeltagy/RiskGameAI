from tkinter import *
class mapEgypt:
    def __init__(self):
        self.ter = [0]
        self.troopNum = [0]
        self.control = [0]
        self.adjacency = [0]
        self.player1Available = 17
        self.player2Available = 17
        self.start()

    def start(self):
        i = 1
        while(i<28):
            self.ter.append(i)
            self.troopNum.append(0)
            self.control.append(0)
            i=i+1


        self.adjacency.append((2, 3, 14, 21))  # 1

        self.adjacency.append((3, 1))  # 2

        self.adjacency.append((1, 2, 4, 9, 10, 14))  # 3

        self.adjacency.append((3, 9, 5))  # 4

        self.adjacency.append((4, 6, 9, 10, 11, 12))  # 5

        self.adjacency.append((5,))  # 6

        self.adjacency.append((13, 8))  # 7

        self.adjacency.append((13, 17, 18))  # 8

        self.adjacency.append((3, 4, 5, 10, 11))  # 9

        self.adjacency.append((3, 9, 5, 11, 14))  # 10

        self.adjacency.append((10, 9, 5, 12, 16, 14))  # 11

        self.adjacency.append((5, 11, 13, 16, 17))  # 12

        self.adjacency.append((12, 7, 8, 17))  # 13

        self.adjacency.append((1, 3, 10, 11, 16, 15, 19, 20, 21))  # 14

        self.adjacency.append((14, 19))  # 15

        self.adjacency.append((14, 11, 12, 17, 23, 19))  # 16

        self.adjacency.append((8, 13, 12, 16, 18, 23))  # 17

        self.adjacency.append((8, 17))  # 18

        self.adjacency.append((14, 15, 16, 20, 23))  # 19

        self.adjacency.append((21, 14, 19, 23, 22))  # 20

        self.adjacency.append((1, 14, 20, 22, 24, 25, 26, 27))  # 21

        self.adjacency.append((20, 21, 23, 24))  # 22

        self.adjacency.append((16, 17, 19, 20, 22, 24, 25, 26, 27))  # 23

        self.adjacency.append((21, 22, 23, 25))  # 24

        self.adjacency.append((21, 24, 23, 26, 27))  # 25

        self.adjacency.append((25,))  # 26

        self.adjacency.append((21, 25, 23))  # 27

    def getInfo(self):
        info = ""
        i=1
        while (i<28):
            controller = "none"
            if(self.control.__getitem__(i) != 0):
                controller = str(self.control.__getitem__(i))

            info = info + "Territory: " + str(i) + " Number of Troops: " + str(self.troopNum.__getitem__(i)) + " Controlled by Player: " + str(controller) + '\n'
            i = i+1
        return info








