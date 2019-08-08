from tkinter import *
class win:
    def __init__(self):
        winner =0

    def win(self , winner , root ):
        root2 = Toplevel()
        l1 = Label(root2, text="Player" + str(winner) + "won")
        l1.pack()

        def finish():

           root.destroy()


        button3 = Button(root2, text="Close", command=finish)
        #button3.grid(row=3, column=1)
        button3.pack()
