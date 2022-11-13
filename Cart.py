from Pizza import Pizza
from Toppings import Toppings
from Side import Side
from Salad import Salad
from Ingredients import Ingredients
from Dessert import Dessert
from Beverage import Beverage
from Order import Order
from Coupons import Coupons
from Product import Product

from datetime import datetime

#----------------------------------------------------
# Cart Class
#----------------------------------------------------

class Cart:
    def __init__(self):
        self._order = None
        self._coupons = None
        self._coupon = None
        self._date = datetime.now()
        self._subTotal = None
        self._tax = .05
        self._total = None
        

#----------------------------------------------------
# order
#----------------------------------------------------

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order):
        self._order = order
        
    def delOrder(self):
        self._order = None
        
#----------------------------------------------------
# coupons
#----------------------------------------------------        

    @property
    def coupons(self):
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        self._coupons = coupons

#----------------------------------------------------
# coupon
#----------------------------------------------------

    @property
    def coupon(self):
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        self._coupon = coupon
        
    def checkCoupon(self):    
        couponBucket = []
        
        for idx, productOrder in enumerate(self._order.products):
            for coupon in self._coupons:
                for couponRequirement in coupon.requirements:
                        
                    if self._order.qty[idx] == couponRequirement.qty and couponRequirement.category == 'Pizza' and productOrder.category == 'Pizza':
                        verified = True
                        if couponRequirement.style != None and couponRequirement.style != productOrder.style:
                            verified = False                            
                        if couponRequirement.size != None and couponRequirement.size != productOrder.size:
                            verified = False
                        if couponRequirement.toppings != None and couponRequirement.toppings != len(productOrder.toppings):
                            verified = False   
                            
                        if verified == True:
                            couponBucket.append(couponRequirement)
                        
                    if self._order.qty[idx] == couponRequirement.qty and couponRequirement.category == 'Side' and productOrder.category == 'Side':
                        verified = True
                        
                        if couponRequirement.size != None and couponRequirement.size != productOrder.size:
                            verified = False
                            
                        if verified == True:
                            couponBucket.append(couponRequirement)

                    if self._order.qty[idx] == couponRequirement.qty and couponRequirement.category == 'Salad' and productOrder.category == 'Salad':
                        verified = True
                        
                        if couponRequirement.size != None and couponRequirement.size != productOrder.size:
                            verified = False
                            
                        if couponRequirement.ingredients != None and len(couponRequirement.ingredients) != len(productOrder.ingredients):
                            verified = False   
                                                
                        if verified == True:
                            couponBucket.append(couponRequirement)

                    if self._order.qty[idx] == couponRequirement.qty and couponRequirement.category == 'Dessert' and productOrder.category == 'Dessert':
                        verified = True
                        
                        if couponRequirement.size != None and couponRequirement.size != productOrder.size:
                            verified = False
                        
                        if verified == True:
                            couponBucket.append(couponRequirement)
                            
                    if self._order.qty[idx] == couponRequirement.qty and couponRequirement.category == 'Beverage' and productOrder.category == 'Beverage':
                        verified = True
                        
                        if couponRequirement.size != None and couponRequirement.size != productOrder.size:
                            verified = False
                        
                        if verified == True:
                            couponBucket.append(couponRequirement)
                
                if len(coupon.requirements) == len(couponBucket):
                    if self.coupon == None or self.coupon.discount < coupon.discount:
                        self._coupon = coupon
                        
#----------------------------------------------------
# date
#----------------------------------------------------

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):
        self._date = date
        
        
#----------------------------------------------------
# sub-total
#----------------------------------------------------  

    @property
    def subTotal(self):
        return self._subTotal   

    @subTotal.setter
    def subTotal(self, subTotal):
        self._subTotal = subTotal
        
    def calcSubTotal(self):
        subTotal = float(0.00)
        for idx, product in enumerate(self.order.products):
            subTotal += self.order.products[idx].price * self.order._qty[idx]
            if product.category == 'Pizza':
                for topping in product.toppings:
                    subTotal += topping.price
            if product.category == 'Salad':
                for ingredient in product.ingredients:
                    subTotal += ingredient.price
                    
        self._subTotal = subTotal
        
#----------------------------------------------------
# tax
#----------------------------------------------------

    @property
    def tax(self):
        return self._tax

    @tax.setter
    def tax(self, value):
        self._tax = value
        
    def calcTax(self):
       self._tax = (self._subTotal - self.coupon.discount) * self._tax

#----------------------------------------------------
# total
#----------------------------------------------------  

    @property
    def total(self):
        return self._total   

    @total.setter
    def total(self, total):
        self._total = total

    def calcTotal(self):
        self.calcSubTotal()
        self.checkCoupon()
        self.calcTax()
        if self.coupon != None:
            self._total = self._subTotal - self.coupon.discount + self._tax
        else:
            self._total = self._subTotal + self._tax

#----------------------------------------------------
# submit
#----------------------------------------------------  

    def submit(self):
        pass
    
#----------------------------------------------------
# repr
#----------------------------------------------------  

    def __repr__(self):
        if self.coupon != None:
            return f'{self._order}, {self._coupon}, {self.date}, Subtotal: ${self._subTotal:.2f}, Tax: ${self._tax:.2f}, Coupon: -${self.coupon.discount:.2f} Total: ${self._total:.2f}'
        else:
            return f'{self._order}, {self._coupon}, {self.date}, Subtotal: ${self._subTotal:.2f}, Tax: ${self._tax:.2f}, Total: ${self._total:.2f}'

#----------------------------------------------------
# str
#----------------------------------------------------  

    def __str__(self):
        if self.coupon != None:
            return f'{self._order}, {self._coupon}, {self.date}, Subtotal: ${self._subTotal:.2f}, Tax: ${self._tax:.2f}, Coupon: -${self.coupon.discount:.2f} Total: ${self._total:.2f}'
        else:
            return f'{self._order}, {self._coupon}, {self.date}, Subtotal: ${self._subTotal:.2f}, Tax: ${self._tax:.2f}, Total: ${self._total:.2f}'
        

