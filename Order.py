from Pizza import Pizza
from Toppings import Toppings
from Side import Side
from Salad import Salad
from Ingredients import Ingredients
from Dessert import Dessert
from Beverage import Beverage

import copy

#----------------------------------------------------
# Order Class
#----------------------------------------------------   

class Order:
    def __init__(self):
        self._orderID = None
        self._products = list()
        self._qty = list()

#----------------------------------------------------
# order ID
#----------------------------------------------------   

    @property
    def orderID(self):
        return self._orderID

    @orderID.setter
    def orderID(self, orderNum):
        self._orderID = orderNum
        
#----------------------------------------------------
# products
#----------------------------------------------------   

    @property
    def products(self):
        return self._products
    
    @products.setter
    def products(self, products):
        self._products = copy.deepcopy(products)

    def addProduct(self, product):
        self._products.append(copy.deepcopy(product))

    def removeProduct(self, idx):
        self._products.pop(idx)

#----------------------------------------------------
# quantity
#----------------------------------------------------  
 
    @property
    def qty(self):
        return self._qty

    @qty.setter
    def qty(self, newQty):
        self._qty = newQty

    def addQty(self, qty):
        self._qty.append(qty)
        
#----------------------------------------------------
# repr
#----------------------------------------------------  

    def __repr__(self):
        for product in self.products:
            if product.category == 'Pizza':
                return f'{self._orderID} {self._products} {self._qty}\n     {self._products.toppings}'
            elif product.category == 'Salad':
                return f'{self._orderID} {self._products} {self._qty}\n     {self._products.ingredients}'
            else: 
                return f'{self._orderID} {self._products} {self._qty}'

#----------------------------------------------------
# str
#----------------------------------------------------  

    def __str__(self):
        return f'Order ID: {self._orderID}\n{self._products} {self._qty}'

        
#----------------------------------------------------
# str
#----------------------------------------------------  
    def __del__(self):
        return 'Order Deleted'

