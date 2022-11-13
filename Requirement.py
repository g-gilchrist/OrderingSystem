#----------------------------------------------------
# Requirements Class
#----------------------------------------------------   

class Requirement():
    def __init__(self):
        self._categories = list()
        self._category = None
        self._sizes = list()
        self.size = None
        self._qty = None
        self._toppings = None
        self._ingredients = None

#----------------------------------------------------
# categories
#----------------------------------------------------   

    @property
    def categories(self):
        return self._categories
    
    @categories.setter
    def categories(self, categories):
        self._categories = categories

    def addCategory(self, category):
        self._sizes.append(category)
        
    def delcategory(self,idx):
        self._categories.pop(idx)
        
#----------------------------------------------------
# category
#----------------------------------------------------   

    @property
    def category(self):
        return self._category
    
    @category.setter      
    def category(self,category):
            self._category = category     

    def setCategory(self,idx):
        try:
            self._category = self._categories[idx]       
        except:
            return 'Error: Numbers only. '

#----------------------------------------------------
# sizes
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
# size
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
# quantity
#----------------------------------------------------   

    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, quantity):
        self._qty = quantity
    
#----------------------------------------------------
# toppings (use this to set a number of toppings)
#----------------------------------------------------   

    @property
    def toppings(self):
        return self._qty

    @toppings.setter
    def toppings(self, qty):
        self._toppings = qty
        
#----------------------------------------------------
# ingredients (use this to set a number of ingredients)
#----------------------------------------------------   

    @property
    def ingredients(self):
        return self._qty

    @ingredients.setter
    def ingredients(self, qty):
        self.ingredients = qty
        
#----------------------------------------------------
# repr
#----------------------------------------------------  

    def __repr__(self):
        return f'{self._category}, {self._size}, {self._qty}, {self._toppings}, {self._ingredients}'

#----------------------------------------------------
# str
#----------------------------------------------------  

    def __str__(self):
        return f'{self._category}, {self._size}, {self._qty}, {self._toppings}, {self._ingredients}'
    
#----------------------------------------------------
# delete requirement
#----------------------------------------------------    
    def __del__(self):
        return 'Requirement Deleted'
