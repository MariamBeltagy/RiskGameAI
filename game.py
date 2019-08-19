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
turns = [0]


def updateAll(listL):
    numList = globals.map.troopNum
    ctrl = globals.map.control
    i=0


    for label in listL:
       color = "white"
       troopNum = 0
       if(i!=0):
           if(ctrl[i] == 1):
               color = "red"
           elif(ctrl[i] == 2):
               color = "blue"

           troopNum = numList[i]

           label.config(text=troopNum , bg=color , fg="white")

       i=i+1





    return


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

    updateAll(listL)



def next(turn, move, infoList):

    if(move[0] == infoList.__len__()-1):

        if (turn[0] == 1):
            num = globals.map.control.count(1)

            num = int(num/3)

            if(num < 3):
                num =3
            globals.map.player1Available += num
            player1.move(1,infoText,listL)
            turns[0]=turns[0]+1
            turn_number.set("Turn " + str(turns[0]))
        else:
            num = globals.map.control.count(2)
            num = int(num / 3)
            if (num  < 3):
                num = 3
            globals.map.player2Available += num
            player2.move(2,infoText,listL)


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

    updateAll(listL)



root = Tk()
root.geometry("1500x900")


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
#l0.grid(row=2,column=2)
l0.place(x=400,y=100)

info = map.getInfo()
infoList = []
infoList.append(info)

infoText = StringVar()
turn_number = StringVar()

infoText.set(info)
l1 = Label(root, textvariable = infoText)
l1.grid(row=2,column=0)

l111 = Label(root, textvariable = turn_number)
l111.grid(row=0,column=0)


move = [0]
turn = [1]


button1 = Button(root, text="previous",command=lambda:prev(turn , move , infoList ))
button1.grid(row=3,column=2)

button2 = Button(root, text="Next",command=lambda:next(turn , move , infoList ))
button2.grid(row=3,column=3)


listL = [0]

############################
if mapName == "usa":
    la1 = Label(root , text= "1")
    la1.place(x= 570, y= 260 )
    listL.append(la1)

    la2 = Label(root , text= "2")
    la2.place(x= 164+375, y= 217+88 )
    listL.append(la2)

    la3 = Label(root , text= "3")
    la3.place(x= 160+375, y= 336+88 )
    listL.append(la3)

    la4 = Label(root , text= "4")
    la4.place(x= 205+375, y= 301+88 )
    listL.append(la4)

    la5 = Label(root , text= "5")
    la5.place(x= 250+375, y= 237+88 )
    listL.append(la5)

    la6 = Label(root , text= "6")
    la6.place(x= 306+375, y= 200+88 )
    listL.append(la6)

    la7 = Label(root , text= "7")
    la7.place(x= 322+375, y= 266+88 )
    listL.append(la7)

    la8 = Label(root , text= "8")
    la8.place(x= 264+375, y= 320+88 )
    listL.append(la8)

    la9 = Label(root , text= "9")
    la9.place(x= 256+375, y= 405+88 )
    listL.append(la9)


    la10 = Label(root , text= "10")
    la10.place(x= 350+375, y= 337+88 )
    listL.append(la10)


    la11 = Label(root , text= "11")
    la11.place(x= 330 + 376, y= 415+88 )
    listL.append(la11)

    la12 = Label(root , text= "12")
    la12.place(x= 416+375, y= 505+88 )
    listL.append(la12)

    la13 = Label(root , text= "13")
    la13.place(x= 465+375, y= 414+88 )
    listL.append(la13)

    la14 = Label(root , text= "14")
    la14.place(x= 442+375, y= 348+88 )
    listL.append(la14)

    la15 = Label(root , text= "15")
    la15.place(x= 430+375, y= 302+88 )
    listL.append(la15)

    la16 = Label(root , text= "16")
    la16.place(x= 435+375, y= 255+88 )
    listL.append(la16)

    la17 = Label(root , text= "17")
    la17.place(x= 427+375, y= 209+88 )
    listL.append(la17)

    la18 = Label(root , text= "18")
    la18.place(x= 460+375, y= 194+88 )
    listL.append(la18)

    la19 = Label(root , text= "19")
    la19.place(x= 505+375, y= 290+88 )
    listL.append(la19)


    la20 = Label(root , text= "20")
    la20.place(x= 520+375, y= 365+88 )
    listL.append(la20)

    la21 = Label(root , text= "21")
    la21.place(x= 517 + 376, y= 396+88 )
    listL.append(la21)

    la22 = Label(root , text= "22")
    la22.place(x= 508+375, y= 455+88 )
    listL.append(la22)

    la23 = Label(root , text= "23")
    la23.place(x= 551+375, y= 420+88 )
    listL.append(la23)

    la24 = Label(root , text= "24")
    la24.place(x= 586+375, y= 448+88 )
    listL.append(la24)

    la25 = Label(root , text= "25")
    la25.place(x= 681+375, y= 531+88 )
    listL.append(la25)

    la26 = Label(root , text= "26")
    la26.place(x= 640+375, y= 450+88 )
    listL.append(la26)

    la27 = Label(root , text= "27")
    la27.place(x= 680+375, y= 423+88 )
    listL.append(la27)

    la28 = Label(root , text= "28")
    la28.place(x= 715+375, y= 375+88 )
    listL.append(la28)

    la29 = Label(root , text= "29")
    la29.place(x= 715+375, y= 350+88 )
    listL.append(la29)


    la30 = Label(root , text= "30")
    la30.place(x= 658+375, y= 325+88 )
    listL.append(la30)


    la31 = Label(root, text="31")
    la31.place(x=613 + 376, y=390 + 88)
    listL.append(la31)

    la32 = Label(root, text="32")
    la32.place(x=580 + 375, y=362 + 88)
    listL.append(la32)

    la33 = Label(root, text="33")
    la33.place(x=545 + 375, y=346 + 88)
    listL.append(la33)

    la34 = Label(root, text="34")
    la34.place(x=510 + 385, y=225 + 88)
    listL.append(la34)

    la35 = Label(root, text="35")
    la35.place(x=580 + 375, y=338 + 88)
    listL.append(la35)

    la36 = Label(root, text="36")
    la36.place(x=590 + 375, y=234 + 88)
    listL.append(la36)

    la37 = Label(root, text="37")
    la37.place(x=630 + 375, y=298 + 88)
    listL.append(la37)

    la38 = Label(root, text="38")
    la38.place(x=705 + 375, y=286 + 88)
    listL.append(la38)

    la39 = Label(root, text="39")
    la39.place(x=680 + 375, y=250 + 88)
    listL.append(la39)

    la40 = Label(root, text="40")
    la40.place(x=735 + 375, y=219 + 88)
    listL.append(la40)

    la41 = Label(root, text="41")
    la41.place(x=750 + 375, y=230 + 88)
    listL.append(la41)

    la42 = Label(root, text="42")
    la42.place(x=775 + 375, y=165 + 88)
    listL.append(la42)

    la43 = Label(root, text="43")
    la43.place(x=820 + 375, y=245 + 88)
    listL.append(la43)

    la44 = Label(root, text="44")
    la44.place(x=820 + 375, y=270 + 88)
    listL.append(la44)

    la45 = Label(root, text="45")
    la45.place(x=810 + 375, y=295 + 88)
    listL.append(la45)

    la46 = Label(root, text="46")
    la46.place(x=775 + 375, y=305 + 88)
    listL.append(la46)

    la47 = Label(root, text="47")
    la47.place(x=775 + 375, y=325 + 88)
    listL.append(la47)

    la48 = Label(root, text="48")
    la48.place(x=705 + 375, y=320 + 88)
    listL.append(la48)

    la49 = Label(root, text="49")
    la49.place(x=152 + 375, y=510 + 88)
    listL.append(la49)

    la50 = Label(root, text="50")
    la50.place(x=109 + 375, y=29 + 88)
    listL.append(la50)
##############################
if mapName == "egypt":
    la1 = Label(root, text="1")
    la1.place(x=570, y=260)
    listL.append(la1)

    la2 = Label(root, text="2")
    la2.place(x=400 + 375, y=81 + 88)
    listL.append(la2)

    la3 = Label(root, text="3")
    la3.place(x=420 + 375, y=141 + 88)
    listL.append(la3)

    la4 = Label(root, text="4")
    la4.place(x=465 + 375, y=49 + 88)
    listL.append(la4)

    la5 = Label(root, text="5")
    la5.place(x=520 + 375, y=66 + 88)
    listL.append(la5)

    la6 = Label(root, text="6")
    la6.place(x=574 + 375, y=16 + 88)
    listL.append(la6)

    la7 = Label(root, text="7")
    la7.place(x=620 + 375, y=35 + 88)
    listL.append(la7)

    la8 = Label(root, text="8")
    la8.place(x=625 + 375, y=120 + 88)
    listL.append(la8)

    la9 = Label(root, text="9")
    la9.place(x=475 + 375, y=95 + 88)
    listL.append(la9)

    la10 = Label(root, text="10")
    la10.place(x=483 + 375, y=125 + 88)
    listL.append(la10)

    la11 = Label(root, text="11")
    la11.place(x=498 + 376, y=145 + 88)
    listL.append(la11)

    la12 = Label(root, text="12")
    la12.place(x=523 + 375, y=130 + 88)
    listL.append(la12)

    la13 = Label(root, text="13")
    la13.place(x=555 + 375, y=133 + 88)
    listL.append(la13)

    la14 = Label(root, text="14")
    la14.place(x=285 + 375, y=308 + 88)
    listL.append(la14)

    la15 = Label(root, text="15")
    la15.place(x=440 + 375, y=225 + 88)
    listL.append(la15)

    la16 = Label(root, text="16")
    la16.place(x=520 + 375, y=175 + 88)
    listL.append(la16)

    la17 = Label(root, text="17")
    la17.place(x=565 + 375, y=222 + 88)
    listL.append(la17)

    la18 = Label(root, text="18")
    la18.place(x=680 + 375, y=285 + 88)
    listL.append(la18)

    la19 = Label(root, text="19")
    la19.place(x=420 + 375, y=245 + 88)
    listL.append(la19)

    la20 = Label(root, text="20")
    la20.place(x=385 + 375, y=320 + 88)
    listL.append(la20)

    la21 = Label(root, text="21")
    la21.place(x=370 + 376, y=452 + 88)
    listL.append(la21)

    la22 = Label(root, text="22")
    la22.place(x=481 + 375, y=371 + 88)
    listL.append(la22)

    la23 = Label(root, text="23")
    la23.place(x=551 + 375, y=360 + 88)
    listL.append(la23)

    la24 = Label(root, text="24")
    la24.place(x=540 + 375, y=425 + 88)
    listL.append(la24)

    la25 = Label(root, text="25")
    la25.place(x=570 + 375, y=460 + 88)
    listL.append(la25)

    la26 = Label(root, text="26")
    la26.place(x=655 + 375, y=510 + 88)
    listL.append(la26)

    la27 = Label(root, text="27")
    la27.place(x=610 + 375, y=650 + 88)
    listL.append(la27)

#############################

 #updateAll(listL)

# def motion(event):
#      x, y = event.x, event.y
#      print('{}, {}'.format(x, y))
#
# root.bind('<Motion>', motion)
root.mainloop()



root.mainloop()