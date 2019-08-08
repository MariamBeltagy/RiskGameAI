import sys
import time
print("try 1,2,5,3,4,0,6,7,8")
print("try 1,4,2,6,5,8,7,3,0")
print("try:1,0,2,7,5,4,8,6,3")
print("try:4,1,3,0,2,6,7,5,8")
class State():
    def __init__(self):
        self.items = []
        self.f = 0
        self.g = 0
        self.d = ""

    def add(self , item):
        self.items = item

    def getState(self):
        return self.items


    def setF(self , item):
        self.f = item

    def getF(self):
        return self.f

    def setG(self, item):
        self.g = item

    def getG(self):
        return self.g

    def setD(self, item):
        self.d = item

    def getD(self):
        return self.d

class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self , item):
        self.items.append(item)

    def dequeue(self):
        item = self.items.__getitem__(0)
        self.items.__delitem__(0)
        return item

    def get_queue(self):
        return self.items

    def first(self):
        return self.items.__getitem__(0)

    def modify(self):
       i=0
       minVal = sys.maxsize
       minIndex = 0
       while(i<self.items.__len__()):
           if(self.items[i].getF() < minVal):
               minVal = self.items[i].getF()
               minIndex = i
           i=i+1
       minState = self.items.__getitem__(minIndex)
       self.items.remove(minState)
       self.items.insert(0, minState)


# Those are functions to ask user to enter elements and functions to get neighbours to right , left , up , down no need
def getCol(item):
    return item%3

def getRow(item):
    return int(item/3)

def insertElement():
    list = []
    i=0
    x = 0
    while(i<9):
        x = input("Enter number " + str(i+1) + " : ")
        list.append(x)
        i=i+1
    return list

def rightState(item):
    list=[];
    list = item.copy()
    index = list.index('0')
    if ((index+1) %3 == 0):
        return None

    a = list.__getitem__(index)
    b = list.__getitem__(index+1)
    list[index] = b
    list[index+1] = a
    return list

def leftState(item):
    list=[];
    list = item.copy()
    index = list.index('0')
    if ((index) %3 == 0 ):
        return None

    a = list.__getitem__(index)
    b = list.__getitem__(index-1)
    list[index] = b
    list[index-1] = a
    return list

def upState(item):
    list=[];
    list = item.copy()
    index = list.index('0')
    if (index-3 < 0 ):
        return None

    a = list.__getitem__(index)
    b = list.__getitem__(index-3)
    list[index] = b
    list[index-3] = a
    return list

def downState(item):
    list=[];
    list = item.copy()
    index = list.index('0')
    if (index+3 > len(list)-1 ):
        return None

    a = list.__getitem__(index)
    b = list.__getitem__(index+3)
    list[index] = b
    list[index+3] = a
    return list

def getCostMan(g,node):
    cost = g
    item =[]
    i=0

    while(i<9):
        x1 = getRow(i)
        y1 = getCol(i)
        x2 = getRow(node.index(str(i)))
        y2 = getCol(node.index(str(i)))
        cost = cost + abs(y2-y1) + abs(x2-x1)
        i=i+1

    return cost


list = []
list = insertElement()
goal = ['0','1','2','3','4','5','6','7','8']
initial = State()
initial.add(list)
initial.setD("initial")
initial.setF(getCostMan(0,list))
initial.setG(0)

frontier = []
frontier.append(list)
directions = []
directions.append("initial")
expanded = []
path = []
s = Queue()
s.enqueue(initial)
top = State()
maxDepth =0
# from here loop to explore elements
start_time = time.time()
while(1):

    top = s.dequeue()

    if (top.getG() > maxDepth):
        maxDepth = g

    if(top.getState() == goal):
        print("Running time to Reach Goal")
        print("--- %s seconds ---" % (time.time() - start_time))
        break

    g = top.getG() +1



    expanded.append(top.getState())

    up = State()
    down = State()
    left = State()
    right = State()

    up.add(upState(top.getState()))
    down.add(downState(top.getState()))
    left.add(leftState(top.getState()))
    right.add(rightState(top.getState()))


    if (up.getState() != None and not(frontier.__contains__(up.getState()))):
        up.setG(g)
        up.setF(getCostMan(g, up.getState()))
        s.enqueue(up)
        frontier.append(up.getState())
        directions.append("up")

    if (down.getState() != None and not (frontier.__contains__(down.getState()))):
        down.setG(g)
        down.setF(getCostMan(g, down.getState()))
        s.enqueue(down)
        frontier.append(down.getState())
        directions.append("down")


    if (left.getState() != None and not (frontier.__contains__(left.getState()))):
        left.setG(g)
        left.setF(getCostMan(g, left.getState()))
        s.enqueue(left)
        frontier.append(left.getState())
        directions.append("left")

    if (right.getState() != None and not(frontier.__contains__(right.getState()))):
        right.setG(g)
        right.setF(getCostMan(g, right.getState()))
        s.enqueue(right)
        frontier.append(right.getState())
        directions.append("right")



    s.modify()






i = frontier.index(goal)
while(1):
    go = directions[i]
    child = frontier[i]
    parent = []
    if(go == "up"):
        parent = downState(child)

    if (go == "down"):
        parent = upState(child)

    if (go == "left"):
        parent = rightState(child)

    if (go == "right"):
        parent = leftState(child)

    path.insert(0,child)

    i = frontier.index(parent)


    if(i ==0):
        path.insert(0,parent)
        break

print("Nodes Expanded :")
print(expanded)
print("Nodes Explored :")
print(frontier)
print("Nodes on Path :")
print(path)
print("Max Depth Search :")
print(maxDepth)


# from here path list is used to move puctures , doesnt need to change
q = [0]
from tkinter import *

root = Tk()
photo0= PhotoImage(file="0.png")
photo1= PhotoImage(file="1.png")
photo2= PhotoImage(file="2.png")
photo3= PhotoImage(file="3.png")
photo4= PhotoImage(file="4.png")
photo5= PhotoImage(file="5.png")
photo6= PhotoImage(file="6.png")
photo7= PhotoImage(file="7.png")
photo8= PhotoImage(file="8.png")


l0 = Label(root, image=photo0)
l1 = Label(root, image=photo1)
l2 = Label(root, image=photo2)
l3 = Label(root, image=photo3)
l4 = Label(root, image=photo4)
l5 = Label(root, image=photo5)
l6 = Label(root, image=photo6)
l7 = Label(root, image=photo7)
l8 = Label(root, image=photo8)





l0.grid(row =0)
l1.grid(row=0,column=1)
l2.grid(row=0,column=2)

l3.grid(row =1)
l4.grid(row=1,column=1)
l5.grid(row=1,column=2)

l6.grid(row =2)
l7.grid(row=2,column=1)
l8.grid(row=2,column=2)




def updateAll(list1 , list2):


    i =0
    l9 = Label(root, text="cost " + str(q[0]))
    l9.grid(row=3,column=3)
    while(i<9):
        index = list1.index(str(i))
        list2.__getitem__(i).grid(row=getRow(index),column=getCol(index))
        i= i+1;





def prev(q,path,labels):
    if(q[0]== 0):
        return None
    q[0]=q[0]-1
    updateAll(path.__getitem__(q[0]),labels)


def next(q,path,labels):

    if(q[0]== len(path)-1):
        return None
    q[0]=q[0]+1
    updateAll(path.__getitem__(q[0]),labels)



labels =[l0,l1,l2,l3,l4,l5,l6,l7,l8]
button1 = Button(root, text="previous",command=lambda:prev(q,path,labels))
button1.grid(row=3,column=0)
button2 = Button(root, text="Next",command=lambda:next(q,path,labels))
button2.grid(row=3,column=1)




updateAll(path.__getitem__(q[0]),labels)
root.mainloop()







