from tkinter import *
class mapUSA:
    def __init__(self):
        self.name = "usa"
        self.ter = [0]
        self.troopNum = [0]
        self.control = [0]
        self.adjacency = []
        self.player1Available = 17
        self.player2Available = 17
        self.start()

    def start(self):
        i = 1
        list = []
        while(i<51):
            self.ter.append(i)
            self.troopNum.append(0)
            self.control.append(0)
            list.append(i)
            i=i+1

        self.adjacency.append(list)


        self.adjacency.append([2,5,50])
        self.adjacency.append([1,3,4,5])
        self.adjacency.append([2,4,9,49])
        self.adjacency.append([2,3,8,9,5])
        self.adjacency.append([1,2,4,6,7,8])
        self.adjacency.append([5,7,16,17])
        self.adjacency.append([5,6,8,10,15,16])
        self.adjacency.append([4,5,7,10,9,11])
        self.adjacency.append([3,4,8,10,11])
        self.adjacency.append([7,8,9,11,13,14,15])
        self.adjacency.append([8,9,10,12,13])
        self.adjacency.append([11,13,21,22])
        self.adjacency.append([12,11,10,14,20,21])
        self.adjacency.append([13,10,15,20])
        self.adjacency.append([14,10,7,16,19,20])
        self.adjacency.append([15,7,6,17,18,19])
        self.adjacency.append([6,16,18])
        self.adjacency.append([17,16,19,34])
        self.adjacency.append([15,16,18,34,33,20])
        self.adjacency.append([19,33,32,31,21,13,14,15])
        self.adjacency.append([13,20,31,23,22,12])
        self.adjacency.append([12,21,23])
        self.adjacency.append([22,21,31,24])
        self.adjacency.append([23,31,26,25])
        self.adjacency.append([24,26])
        self.adjacency.append([25,24,31,28,27])
        self.adjacency.append([26,28])
        self.adjacency.append([27,26,31,29])
        self.adjacency.append([28,31,32,30,48])
        self.adjacency.append([29,32,37,38,48])
        self.adjacency.append([20,21,23,24,26,28,29,32])
        self.adjacency.append([33,35,37,30,29,31,20])
        self.adjacency.append([20,19,34,36,32])
        self.adjacency.append([18,19,33,36])
        self.adjacency.append([33,32,37,36])
        self.adjacency.append([34,35,37])
        self.adjacency.append([36,35,32,30,38])
        self.adjacency.append([37,30,48,47,46,39])
        self.adjacency.append([38,46,45,43,40])
        self.adjacency.append([39,41,43])
        self.adjacency.append([42,43,40])
        self.adjacency.append([41])
        self.adjacency.append([41,40,39,44,45])
        self.adjacency.append([43,45])
        self.adjacency.append([44,43,39])
        self.adjacency.append([47,38,39])
        self.adjacency.append([46,48,38])
        self.adjacency.append([29,30,38,46])
        self.adjacency.append([3,9])
        self.adjacency.append([1])


    def getInfo(self):
        info = ""
        i=1
        while (i<51):
            controller = "none"
            if(self.control.__getitem__(i) != 0):
                controller = str(self.control.__getitem__(i))
            info = info + "Territory: " + str(i) + " Number of Troops: " + str(self.troopNum.__getitem__(i)) + " Controlled by Player: " + str(controller) + '\n'
            i = i+1
        return info