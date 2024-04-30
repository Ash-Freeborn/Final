from priorityQueue import *
from linkedList import *
from inventory import *
import tkinter as tk

#setting up GUI
root = tk.Tk()
items = []
ids = []
itemsList = LinkedList()
prioritylist = Priority()
root.geometry("500x350")

#Title
title= tk.Label(root,text="Inventory")
title.pack()

def updateOutputBox():
    clear()
    for item in items:
        box.insert("end",item)

    
def clear():
    box.delete(0,"end")

def add():
    item = textinput.get()
    items.append(item)
    updateOutputBox()
    itemsList.add(item)

def addID():
    idNum = textinput.get()
    ids.append(idNum)

def removeAll():
    global items
    items = []
    updateOutputBox()

def remove():
    item = box.get("active")
    if item in items:
        items.remove(item)
    updateOutputBox()
    itemsList.delete(item)

def sort():
    prioritylist.push(itemsList,ids)
    updateOutputBox()




textinput = tk.Entry(root, width=60)
textinput.pack()

box = tk.Listbox(root, width=70)
box.pack()

Add = tk.Button(root, text="Add Item", command=add)
Add.pack()

AddID = tk.Button(root, text="Add ID", command=addID)
AddID.pack()

RemoveAll = tk.Button(root, text="Remove All", command=removeAll)
RemoveAll.pack()

Remove = tk.Button(root, text="Remove",  command=remove)
Remove.pack()

Sort = tk.Button(root, text="Sort", command= sort)
Sort.pack()



close = tk.Button(root, text="Close", command=exit)
close.pack()



root.mainloop()