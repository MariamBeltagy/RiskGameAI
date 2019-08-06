from tkinter import *
import globals
from mapUSA import mapUSA
from mapEgypt import mapEgypt
from win import win
import choice

ended = [0]
map = globals.map
player1 = globals.player1
player2 = globals.player2
def prev(turn ,move, infoList ):

    if(move[0]== 0):
        return None


    move[0] = move [0] -1

    if (move[0] == 0):
        turnText.set("Risk Game - Initial State")
        turn[0] = 1
    elif(turn[0] == 1):
        turn[0] = 2
        turnText.set("Player One Turn")
    else:
        turn[0] =1
        turnText.set("Player Two Turn")


    infoText.set(infoList[move[0]])



def next(turn, move, infoList):

    if(move[0] == infoList.__len__()-1):

        if (turn[0] == 1):
            num = globals.map.control.count(1)
            num = int(num/3)

            if(num/3 < 3):
                num =3
            globals.map.player1Available += num
            player1.move(1,infoText)

        else:
            num = globals.map.control.count(2)
            num = int(num / 3)
            if (num / 3 < 3):
                num = 3
            globals.map.player2Available += num
            player2.move(2,infoText)


        infoList.append(globals.map.getInfo())


    move[0] = move[0] + 1
    if (turn[0] == 1):
        turn[0] = 2
        turnText.set("Player One Turn")
    else:
        turn[0] = 1
        turnText.set("Player Two Turn")


    infoText.set(infoList[move[0]])

    num = globals.map.control.count(1)
    if (num >= 50 and mapName == "usa"):
        winner = win()
        winner.win(1,root)



    if (num >= 27 and mapName == "egypt"):
        winner = win()
        winner.win(1,root)



    num = globals.map.control.count(2)
    if (num >= 50 and mapName == "usa"):
        winner = win()
        winner.win(2,root)



    if (num >= 27 and mapName == "egypt"):
        winner = win()
        winner.win(2,root)



root = Tk()

photo= 0
mapName =0
if(map == "usa"):
    photo = PhotoImage(file="usa.png")
    map = mapUSA()
    globals.map= map
    mapName = "usa"

if(map == "egypt"):
    photo = PhotoImage(file="egypt.png")
    map = mapEgypt()
    globals.map = map
    mapName = "egypt"

turnText = StringVar()
turnText.set("Risk Game - Initial State")
l2 = Label(root, textvariable=turnText)
l2.grid(row=0,column=2)

l0 = Label(root, image=photo)
l0.grid(row=2,column=2)

info = map.getInfo()
infoList = []
infoList.append(info)

infoText = StringVar()
infoText.set(info)
l1 = Label(root, textvariable = infoText)
l1.grid(row=2,column=0)


move = [0]
turn = [1]


button1 = Button(root, text="previous",command=lambda:prev(turn , move , infoList ))
button1.grid(row=3,column=2)

button2 = Button(root, text="Next",command=lambda:next(turn , move , infoList ))
button2.grid(row=3,column=3)


root.mainloop()