from Cart import Cart
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
from PaymentMethod import PaymentMethod
from Orders import Orders

# -------------------------------------------------------------------------------------------#
#                                 Payment Processing Class                                   #
# -------------------------------------------------------------------------------------------#

class PaymentProcessing(Orders):
    def __inti__(self):
        super().__init__()

        self._paymentMethod = None
        self._order = None
        self._receipt = None
        
        self.addOrder() 

# -------------------------------------------------------------------------------------------#
#                                          payment                                           #
# -------------------------------------------------------------------------------------------#

    @property       
    def paymentMethod(self):
        try:
            return self._paymentMethod
        except:
            return 'Payment can not be processed! Please try again. '

    @paymentMethod.setter
    def paymentMethod(self, paymentMethod):
        self._paymentMethod = paymentMethod

# -------------------------------------------------------------------------------------------#
#                                          order                                             #
# -------------------------------------------------------------------------------------------#
 
    @property  
    def order(self):
       try:
           return self._order
       except:
           return 'Submit order again.'
        
    @order.setter
    def order(self, order):
        self._order = order
           
# -------------------------------------------------------------------------------------------#
#                                          submit                                            #
# -------------------------------------------------------------------------------------------#

    def submit(self):
        paid = self.processPayment()
        if paid is True:
            self.receipt()

# -------------------------------------------------------------------------------------------#
#                                          receipt                                           #
# -------------------------------------------------------------------------------------------#

    def receipt(self):

        products = list()
        for idx, product in enumerate(self._order.order.products):
            if product.category == 'Pizza':
                products.append(f'{self.order.order.qty[idx]} - {product.title}: ${product.price:.2f} {product.toppings}')
            elif product.category == 'Salad':
                products.append(f'{self.order.order.qty[idx]} - {product.title}: ${product.price:.2f} {product.ingredients}')
            else: 
                products.append(f'{self.order.order.qty[idx]} - {product.title}: ${product.price:.2f}')


        if self.order.coupon != None:
            return f'''
        
            RECEIPT:
            Order ID: {self._order.order.orderID}
            Date: {self._order.date}
            ------------------------------------------------
            {products}
            ------------------------------------------------
            Coupon: {self.order.coupon.title} 
            
            Sub-total: ${self.order.subTotal:.2f}
            Discount: -${self.order.coupon.discount:.2f}
            Tax: ${self.order.tax:.2f}
            Total: ${self.order.total:.2f}
            
            ''' 
        else:
            return f'''
        
            RECEIPT:
            Order ID: {self._order.orderID}
            Date: {self._order.date}
            ------------------------------------------------
            {products}
            ------------------------------------------------
            
            Sub-total: ${self.order.subTotal:.2f}
            Tax: ${self.order.tax:.2f}
            Total: ${self.order.total:.2f}
            
            ''' 
        

# -------------------------------------------------------------------------------------------#
#                                         processPayment                                     #
# -------------------------------------------------------------------------------------------#
# To connect to the payment API this should take arguments about the order total and payment method as to verify the cc info given is the same on file with the bank.
# This is out of scope for this assignment so we are just passing the method as True, normally the payment API would validate and return an error or perhaps just a boolean

    def processPayment(self):
        pass # ------------------------- This would connect to the payment API and process the payment, which is out of scope for this project
        return True


# -------------------------------------------------------------------------------------------#
#                                           repr                                             #
# -------------------------------------------------------------------------------------------#

    def __repr__(self):
        return f'{self.payment}, {self.order}, {self.receipt()}'

# -------------------------------------------------------------------------------------------#
#                                           str                                              #
# -------------------------------------------------------------------------------------------#

    def __str__(self):
        return f'{self.payment}, {self.order}, {self.receipt()}'

