from Product import Product
from Toppings import Toppings

import copy


#----------------------------------------------------
# category (sets category for Parent Class Product)
#----------------------------------------------------

class Pizza(Product):
    def __init__(self):
        super().__init__()

        self._styles = list()
        self._style = None
        self._sizes = list()
        self._size = None
        self._sauces = list()
        self._sauce = None
        self._toppings = list()
        
        self.setPizzaCat()              
        

#----------------------------------------------------
# category (sets category for Parent Class Product)
#----------------------------------------------------
         
    def setPizzaCat(self):
        self.setCategory(0)                         
                                 
#----------------------------------------------------
# styles
#----------------------------------------------------
     
    @property
    def styles(self):                        
        return self._styles
    
    @styles.setter
    def styles(self, styles):
        self._styles = styles

    def addStyle(self, style):
        self._styles.append(style)
        
    def delStyle(self,idx):
        self._styles.pop(idx)

                    
#----------------------------------------------------
# style
#----------------------------------------------------
     
    @property
    def style(self):                        
        return self._style
    
    @style.setter
    def style(self, style):
        self._style = style
        
    def setStyle(self, idx):
        self._style = self._styles[idx]
        
#----------------------------------------------------
#   sizes
#----------------------------------------------------

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
        
#----------------------------------------------------
#   size 
#----------------------------------------------------

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size
    
    def setSize(self, idx):
        self._size = self._sizes[idx]
        
#----------------------------------------------------
#   sauces
#----------------------------------------------------
        
    @property    
    def sauces(self): 
        return self._sauces
    
    @sauces.setter
    def sauces(self, sauces):
        self._sauces = sauces 
    
    def addSauce(self, sauce):
        self._sauces.append(sauce)
        
    def delSauce(self,idx):
        self._sauces.pop(idx)

    
#----------------------------------------------------
#   sauce
#----------------------------------------------------

    @property    
    def sauce(self): 
        return self._sauce
    
    @sauce.setter
    def sauce(self, sauce):
        self._sauce = sauce
        
    def setSauce(self, idx):
        self._sauce = self._sauces[idx]
        
#----------------------------------------------------
#   toppings 
#----------------------------------------------------
    
    @property
    def toppings(self):
        return self._toppings
    
    @toppings.setter
    def toppings(self, toppings):
        self._toppings = copy.deepcopy(toppings)
       
    def addTopping(self, topping):
        self.toppings.append(copy.deepcopy(topping))

   
#----------------------------------------------------
#   repr
#----------------------------------------------------      
           
    def __repr__(self):
        return f'{self.category}, {self.title}, {self.imgSrc}, {self.description}, ${self.price:.2f}, {self._style}, {self._size}, {self._sauce}, {self._toppings}'
    
#----------------------------------------------------
#   str
#----------------------------------------------------          
    
    def __str__(self):
        return f'{self.category}, {self.title}, {self.imgSrc}, {self.description}, ${self.price:.2f}, {self._style}, {self._size}, {self._sauce}, {self._toppings}'
 

