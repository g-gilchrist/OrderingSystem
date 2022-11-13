from Topping import Topping


#----------------------------------------------------
# Ingredients Class
#----------------------------------------------------  

class Ingredients():
    def __init__(self):
        self._ingredient = None
        self._ingredients = list()

#----------------------------------------------------
# ingredients
#----------------------------------------------------      
    @property    
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self,ingredients):
       self._ingredients = ingredients
            
    def addTopping(self):
        self.newIngredient()
        self._ingredients.append(self._ingredient)
        
    def delTopping(self,idx):
        self._ingredients.pop(idx)
        
#----------------------------------------------------
# ingredient
#----------------------------------------------------

    @property    
    def ingredient(self):
        return self._ingredient

    @ingredient.setter
    def ingredient(self,ingredient):
       self._ingredient = ingredient

    def newIngredient(self):
        self._ingredient = Topping()
        
   
#----------------------------------------------------
# getitem (returns index of Ingredients)
#----------------------------------------------------
            
    def __getitem__(self, idx):
        return self._ingredients[idx]            

#----------------------------------------------------
# delete Ingredients
#----------------------------------------------------  
#Little Bobby Drop Tables says don't utilize this method

    # def __del__(self):
    #     return 'Ingredients Deleted'

