"""

Name : DataStuctureFinal
Author: Ash
Created : 4/30/2024
Course: CIS 152 - Data Structure
Version: 1.0
OS: windows
IDE:  Visual Studio 
Copyright : This is my own original work 
based onspecifications issued by our instructor
Description : An app that allows users to add and remove items
           Input: user input
           Ouput: output gui box
Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""
class LinkedList:
    def __init__(self) -> None:
        self.head = -1
        self.tail = -1
        self.items = []

    def is_empty(self):
        return self.items == 0
    
    def add(self, item):#insert
        self.items.append(item)
        self.tail += 1#update tail

    def peek(self):#peek
        item_str = ''
        if not self.is_empty():
            item_str = self.items[self.head]
            return item_str
        else: 
            return ("List is empty")

    def delete(self,item):#delete
        if not self.is_empty(): #check if empty
            self.peek()
            self.head -= 1 # update head
        else:
            return("List is empty")
        
    def size(self): #size
        return len(self.items)# size of items
    
    def print(self):#prin
        listPrint = []
        for i in self.items:#for item in list print item
         
            listPrint.append(self.peek())# peek item and add to string
            
            return listPrint
        else:
            return ("List is empty")
        
        





    