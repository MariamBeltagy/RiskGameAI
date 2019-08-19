from tkinter import *
import globals
from Agent1 import Agent1
from Agent2 import Agent2
from Agent3 import Agent3
from Agent4 import Agent4
from Agent5 import Agent5
from Agent6 import Agent6
from Agent7 import Agent7
from Agent8 import Agent8

def start():
    root.destroy()

def choice(num):

    if(num==0):
        globals.map = "usa"

    if(num==1):
        globals.map = "egypt"


def choiceP1(num):

    if(num==1):
        globals.player1 = Agent1()

    if(num==2):
        globals.player1 = Agent2()

    if(num==3):
        globals.player1 = Agent3()

    if(num==4):
        globals.player1 = Agent4()

    if(num==5):
        globals.player1 = Agent5()

    if(num==6):
        globals.player1 = Agent6()

    if(num==7):
        globals.player1 = Agent7()

    if(num==8):
        globals.player1 = Agent8()


def choiceP2(num):
    if (num == 1):
        globals.player2 = Agent1()

    if (num == 2):
        globals.player2 = Agent2()


    if (num == 3):
        globals.player2 = Agent3()

    if (num == 4):
        globals.player2 = Agent4()

    if (num == 5):
        globals.player2 = Agent5()

    if (num == 6):
        globals.player2 = Agent6()

    if (num == 7):
        globals.player2 = Agent7()

    if (num == 8):
        globals.player2 = Agent8()



root = Tk()


l0 = Label(root, text = "Choose a Map")
l0.grid(row=0,column=2)

button0 = Button(root, text="USA",command=lambda:choice(0))
button0.grid(row=1,column=1)

button00 = Button(root, text="Egypt",command=lambda:choice(1))
button00.grid(row=1,column=2)

l0 = Label(root, text = "Choose  Players")
l0.grid(row=2,column=2)

l0 = Label(root, text = "Player 1" , fg="red")
l0.grid(row=3,column=0)

button1 = Button(root, text="Human",command=lambda:choiceP1(1))
button1.grid(row=4,column=0)

button2 = Button(root, text="passive",command=lambda:choiceP1(2))
button2.grid(row=5,column=0)

button3 = Button(root, text="Agressive",command=lambda:choiceP1(3))
button3.grid(row=6,column=0)

button4 = Button(root, text="nearily pacifist",command=lambda:choiceP1(4))
button4.grid(row=7,column=0)

button5 = Button(root, text="Greedy",command=lambda:choiceP1(5))
button5.grid(row=8,column=0)

button6 = Button(root, text="A *",command=lambda:choiceP1(6))
button6.grid(row=9,column=0)

button7 = Button(root, text="RT A*",command=lambda:choiceP1(7))
button7.grid(row=10,column=0)

button8 = Button(root, text="Minimax",command=lambda:choiceP1(8))
button8.grid(row=11,column=0)


l11 = Label(root, text = "Player 2" , fg="blue")
l11.grid(row=3,column=2)

button11 = Button(root, text="Human",command=lambda:choiceP2(1))
button11.grid(row=4,column=2)

button21 = Button(root, text="passive",command=lambda:choiceP2(2))
button21.grid(row=5,column=2)

button31 = Button(root, text="Agressive",command=lambda:choiceP2(3))
button31.grid(row=6,column=2)

button41 = Button(root, text="nearily pacifist",command=lambda:choiceP2(4))
button41.grid(row=7,column=2)

button51 = Button(root, text="Greedy",command=lambda:choiceP2(5))
button51.grid(row=8,column=2)

button61 = Button(root, text="A *",command=lambda:choiceP2(6))
button61.grid(row=9,column=2)

button71 = Button(root, text="RT A*",command=lambda:choiceP2(7))
button71.grid(row=10,column=2)

button81 = Button(root, text="Minimax",command=lambda:choiceP2(8))
button81.grid(row=11,column=2)



button82 = Button(root, text="Start Game",command=lambda:start())
button82.grid(row=12,column=1)



root.mainloop()



