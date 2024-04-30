class inventory:
    def __init__(self, itemNum, itemTitle, cost, depart,dateAdded) -> None:
        self.itemNum = itemNum
        self.itemTitle = itemTitle
        self.cost = cost
        self.depart = depart
        self.dateAdded = dateAdded

    @property
    def itemNum(self):
        return self._itemNum
    
    @itemNum.setter
    def itemNum(self, value):
        self._itemNum =value

    @property
    def itemTitle(self):
        return self._itemTitle
    
    @itemTitle.setter
    def itemTitle(self, value):
        self._itemTitle =value

    @property
    def cost(self):
        return self._cost
    
    @cost.setter
    def cost(self, value):
        self._cost =value

    @property
    def depart(self):
        return self._depart
    
    @depart.setter
    def depart(self, value):
        self._depart =value

    @property
    def dateAdded(self):
        return self._dateAdded
    
    @dateAdded.setter
    def dateAdded(self, value):
        self._dateAdded =value

    def display(self,itemNum,itemTitle,cost,depart,dateAdded):
        return (f"Invertory[Quantity: {itemNum}, Title: {itemTitle}, Cost: ${cost}, Dempartment: {depart}, Date Added: {dateAdded}]")