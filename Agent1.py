import globals
from tkinter import *
class Agent1:
    def __init__(self):
        self.map = globals.map
        self.attacks = 0
        self.troops = 0
        self.enemy =0
        self.me = 0

    def move(self , num , infoText , listL):
        self.attacks = 0
        def updateAll(listL):
            numList = globals.map.troopNum
            ctrl = globals.map.control
            i = 0

            for label in listL:
                color = "white"
                troopNum = 0
                if (i != 0):
                    if (ctrl[i] == 1):
                        color = "red"
                    elif (ctrl[i] == 2):
                        color = "blue"

                    troopNum = numList[i]

                    label.config(text=troopNum, bg=color, fg="white")

                i = i + 1

            return
        root2 = Toplevel()
        self.me = num
        if(num == 1):
            self.troops = globals.map.player1Available
            self.enemy =2

        if (num == 2):
            self.troops = globals.map.player2Available
            self.enemy =1
        troopNum = StringVar()
        troopNum.set(str(self.troops))
        l10 = Label(root2, text="troop Available")
        l10.pack()
        l9 = Label(root2, textvariable = troopNum)
        # l0.grid(row=0,column=0)
        l9.pack()
        l0 = Label(root2, text="from (To move from Available type 0)")
        #l0.grid(row=0,column=0)
        l0.pack()
        fromTer = StringVar()
        fromBox = Entry(root2 , textvariable = fromTer)
        #fromBox.grid(row = 0 , column =1)
        fromBox.pack()

        l1 = Label(root2, text="to")
        #l1.grid(row=1,column=0)
        l1.pack()
        toTer = StringVar()
        toBox = Entry(root2, textvariable=toTer)
        #toBox.grid(row=1, column=1)
        toBox.pack()

        l2 = Label(root2, text="Number of Troops to move")
        #l2.grid(row=2,column=0)
        l2.pack()



        numArmy = StringVar()
        numBox = Entry(root2, textvariable=numArmy)
        #numBox.grid(row=2, column=1)
        numBox.pack()
        def doit():
            fro = int(fromTer.get())
            to = int(toTer.get())
            num = int(numArmy.get())
            if( self.validate(fro,to,num) ):
                if(fro==0):
                    troopNum.set(str(int(troopNum.get())-num))
                self.updateMap(fro,to,num)
                infoText.set(globals.map.getInfo())
                updateAll(listL)

        def finish():
           self.attacks =0
           root2.destroy()


        button3 = Button(root2, text="Move", command=doit)
        #button3.grid(row=3, column=1)
        button3.pack()

        button2 = Button(root2, text="Finished", command=lambda: finish())
        #button2.grid(row=4, column=1)
        button2.pack()





    def validate(self , fro ,to ,num):
        if(num > self.troops and fro ==0):
            return False
        map = globals.map
        adj = globals.map.adjacency

        ctrl = globals.map.control
        numList = globals.map.troopNum
        if(fro == 0):
            print("hi")
            if(ctrl[to] != self.enemy):
                return True

            if (ctrl[to] == self.enemy and self.troops >= num and num > numList[ to] and self.attacks == 0):
                self.attacks = 1
                return True




        if(adj[fro].__contains__(to) and not (ctrl[to] == self.enemy) and numList[fro] > num):
            return True


        if (adj[fro].__contains__(to) and ctrl[to]== self.enemy and numList[fro] > num and num > numList[to] and self.attacks ==0 and fro!=0):
            self.attacks =1
            return True





        return False


    def updateMap(self , fro ,to ,num):

        map = globals.map
        adj = globals.map.adjacency
        ctrl = globals.map.control

        numList = globals.map.troopNum
        if(ctrl[to] == self.enemy):
            numList[to] = num
        else:
            numList[to] += num
        ctrl[to] = self.me

        if(fro ==0 and self.me ==1):
            globals.map.player1Available = map.player1Available - num

        if (fro == 0 and self.me == 2):
            globals.map.player2Available = map.player2Available - num

        if(fro != 0):
            numList[fro] = numList[fro] - num

        if(fro ==0):
         self.troops = self.troops - num



        return


