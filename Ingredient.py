#----------------------------------------------------
# Ingredient Class
#----------------------------------------------------   

class Ingredient():
    def __init__(self):
        self._title = None
        self._portion = None
        self._price = None
        
#----------------------------------------------------
# title
#----------------------------------------------------

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        self._title = title

        
#----------------------------------------------------
# portion
#----------------------------------------------------
    @property
    def portion(self):
        return self._portion
    
    @portion.setter
    def portion(self,portion):
        self._portion = portion
        
    def setPortion(self,idx):
        ingredientPortion = ['None', 'Normal', 'Extra']
        self._portion = ingredientPortion[idx]

#----------------------------------------------------
# price
#----------------------------------------------------
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        try:
            if self._portion == 'None':
                self._price = 0
            elif self._portion == 'Normal':       
                self._price = float(price)
            elif self._portion == 'Extra':      
                self._price = round(float((price*1.5)),2)
        except:
            return 'Error: Prices must be numbers'
        
#----------------------------------------------------
# ingredient (returns object)
#----------------------------------------------------
    
    @property
    def ingredient(self):
        return self
          
#----------------------------------------------------
# repr
#----------------------------------------------------                      
    def __repr__(self):
        return f'{self.title}, {self.portion}, ${self.price:.2f}'
    
#----------------------------------------------------
# str
#----------------------------------------------------            
    def __str__(self):
        return f'{self.title}, {self.portion}, ${self.price:.2f}'
    
#----------------------------------------------------
# delete ingredient
#----------------------------------------------------    
    def __del__(self):
        return 'Ingredient Deleted'
    


