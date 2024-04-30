from priorityQueue import *
from linkedList import LinkedList
from inventory import *

if __name__ == "__main__":
    item1 = inventory(4,"Blue Chair",14.99,"Furniture","4/30/2024")
    item2 = inventory(8,"Red Chair",14.99,"Furniture","4/31/2024")
    item3 = inventory(1,"Yellow Chair",14.99,"Furniture","4/29/2024")
    item4 = inventory(9,"Green Chair",14.99,"Furniture","4/29/2024")
    item5 = inventory(5,"Pink Chair",14.99,"Furniture","4/28/2024")
    item6 = inventory(3,"Black Chair",14.99,"Furniture","4/27/2024")

    fakeStore = LinkedList()
    fakeStore.add(item1)
    fakeStore.add(item2)
    fakeStore.add(item3)
    

    print(fakeStore.print())


