from Product import Product
from Ingredients import Ingredients
import copy

class Salad(Product):
    def __init__(self):
        super().__init__()
        self._dressings = list()
        self._dressing = None
        self._sizes =None
        self._size = None   
        self._ingredients = None
      
        self.setSaladCat()
        
        
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
# category (sets category for Parent Class Product)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _      

    def setSaladCat(self):
        self.setCategory(2)
    
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        
#   dressings
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _     
        
    @property    
    def dressings(self): 
        return self._dressings
    
    @dressings.setter
    def dressings(self, dressings):
        self._dressings = dressings
    
    def addDressing(self, dressing):
        self._dressings.append(dressing)
        
    def delDressing(self,idx):
        self._dressings.pop(idx)

    
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        
#   dressing
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    @property    
    def dressing(self): 
        return self._dressing
    
    @dressing.setter
    def dressing(self, dressing):
        self._dressing = dressing
        
    def setDressing(self, idx):
        self._dressing = self._dressings[idx]
        
        
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
        
        
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _        
#   ingredients (In process of confirming status of connection for ingredients)
#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
    
    def setIngredients(self, ingredients):
        self._ingredients = copy.deepcopy(ingredients)      
        

#----------------------------------------------------------------        
           
    def __repr__(self):
        return f'{self.category}, {self.title}, {self.imgSrc}, {self.description}, ${self.price:.2f}, {self._dressing}, {self._size}, {self._ingredients}'
    
#----------------------------------------------------------------        
    
    def __str__(self):
        return f'{self.category}, {self.title}, {self.imgSrc}, {self.description}, ${self.price:.2f}, {self._dressing}, {self._size}, {self._ingredients}'

