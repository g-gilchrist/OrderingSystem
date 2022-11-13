#----------------------------------------------------
# Orders Class
#----------------------------------------------------   

class Orders:
    def __init__(self):
        self._orders = list()

#----------------------------------------------------
# orders
#----------------------------------------------------   

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, orders):
        self._orders = orders       
        
    def addOrder(self, order):
        self._orders.append(order)
        
#----------------------------------------------------
# complete order
#----------------------------------------------------   

    def completeOrder(self, orderIdx):
        self._orders.pop(orderIdx)
        print('Order Complete!')
        
#----------------------------------------------------
# cancel order
#----------------------------------------------------   

    def cancelOrder(self, orderIdx):
        self._orders.pop(orderIdx)
        print('Order Cancelled.')


#----------------------------------------------------
# repr
#----------------------------------------------------   

    def __repr__(self):
        return f'{self.orders}'

#----------------------------------------------------
# str
#----------------------------------------------------   
    def __str__(self):
        return f'{self.orders}'


