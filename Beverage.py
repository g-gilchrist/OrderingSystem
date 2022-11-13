from Product import Product

class Beverage(Product):
    def __init__(self):
        super().__init__()
        self._size=None
        self.setBevCat()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
# category (sets category for Parent Class Product)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    def setBevCat(self):
        self.setCategory(4)
        
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        
#   sizes
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        

    @property
    def sizes(self):
        return self._sizes
    
    @sizes.setter
    def sizes(self, sizes):
        self._sizes = sizes

    def addSize(self, size):
        self._sizes.append(size)
        
    def delSize(self,idx):
        self._sizes.pop(idx)
        
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        
#   size 
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
    
    def setSize(self, idx):
        self._size = self._sizes[idx]
        
