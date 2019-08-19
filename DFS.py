import time

print("try 1,2,5,3,4,0,6,7,8")
class Stack():
    def __init__(self):
        self.items = []

    def push(self , item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def get_stack(self):
        return self.items

    def top(self):
        return self.items.__getitem__(self.items.__len__()-1)

# Those are functions to ask user to enter elements and functions to get neighbours to right , left , up , down no need
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




list = []
list = insertElement()
goal = ['0','1','2','3','4','5','6','7','8']
frontier = []
frontier.append(list)
expanded= []
path = []
s = Stack()
s.push(list)
maxDepth = 0
depth = 0
# from here loop to explore elements
start_time = time.time()
while(1):
    top = s.top()

    if(path.__contains__(top)):
        s.pop()
        depth = depth -1
        path.remove(top)

        continue


    expanded.append(top)
    path.append(top)


    right = rightState(top)
    left = leftState(top)
    up = upState(top)
    down = downState(top)



    if (down != None and not (frontier.__contains__(down))):
        s.push(down)
        frontier.append(down)

    if (right != None and not(frontier.__contains__(right))):
        s.push(right)
        frontier.append(right)

    if (left != None and not(frontier.__contains__(left))):
        s.push(left)
        frontier.append(left)



    if (up != None and not(frontier.__contains__(up))):
        s.push(up)
        frontier.append(up)

    depth = depth+1
    if(depth > maxDepth):
        maxDepth = depth
    current = s.top()
    #print(current)

    if(current==goal):
        path.append(goal)
        print("Running time to Reach Goal")
        print("--- %s seconds ---" % (time.time() - start_time))
        break


print("Nodes Expanded:")
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


def getCol(item):
    return item%3

def getRow(item):
    return int(item/3)

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







