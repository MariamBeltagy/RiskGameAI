from tkinter import *


def choice(num):
    root.destroy()
    if (num == 0):
        pass

    if (num == 1):
        pass

    if (num == 2):
        pass

    if (num == 3):
        pass


root = Tk()

l0 = Label(root, text="Choose an Algorithm")
l0.grid(row=0, column=2)

button1 = Button(root, text="DFS", command=lambda: choice(0))
button1.grid(row=1, column=0)

button2 = Button(root, text="BFS", command=lambda: choice(1))
button2.grid(row=1, column=1)

button3 = Button(root, text="A* (Manhattan Distance)", command=lambda: choice(2))
button3.grid(row=1, column=2)

button4 = Button(root, text="A* (Euclidean Distance)", command=lambda: choice(3))
button4.grid(row=1, column=3)

root.mainloop()
