from tkinter import *
import globals

def choice(num):
    root.destroy()
    if(num==0):
        globals.map = "usa"

    if(num==1):
        globals.map = "egypt"





root = Tk()


l0 = Label(root, text = "Choose an Map")
l0.grid(row=0,column=2)

button1 = Button(root, text="USA",command=lambda:choice(0))
button1.grid(row=1,column=1)

button2 = Button(root, text="Egypt",command=lambda:choice(1))
button2.grid(row=1,column=2)



root.mainloop()



