from Topping import Topping


#----------------------------------------------------
# Toppings Class
#----------------------------------------------------  

class Toppings():
    def __init__(self):
        self._topping = None
        self._toppings = list()

#----------------------------------------------------
# toppings
#----------------------------------------------------      
    @property    
    def toppings(self):
        return self._toppings

    @toppings.setter
    def toppings(self,toppings):
       self._toppings = toppings
            
    def addTopping(self):
        self.newTopping()
        self._toppings.append(self._topping)
        
    def delTopping(self,idx):
        self._toppings.pop(idx)
        
#----------------------------------------------------
# topping
#----------------------------------------------------

    @property    
    def topping(self):
        return self._topping

    @topping.setter
    def topping(self,topping):
       self._topping = topping

    def newTopping(self):
        self._topping = Topping()
        
   
#----------------------------------------------------
# getitem (returns index of Toppings)
#----------------------------------------------------
            
    def __getitem__(self, idx):
        return self._toppings[idx]            

#----------------------------------------------------
# delete Toppings
#----------------------------------------------------  
#Little Bobby Drop Tables says don't utilize this method

    # def __del__(self):
    #     return 'Toppings Deleted'

