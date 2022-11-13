from User import User;
from PaymentMethod import PaymentMethod
# from PaymentProcessing import PaymentProcessing

#----------------------------------------------------
# Customer Class (User Child)
#---------------------------------------------------- 

class Customer(User):
    def __init__(self):
        super().__init__()
        self._paymentMethod = None
        self._paymentMethods = list()
        self._orderHistory = list()    
        
        self.setCustomer()

#----------------------------------------------------
# setCustomer (Sets User Permissions as Customer)
#---------------------------------------------------- 

    def setCustomer(self):
        self.setPermissions(0) 
    
#----------------------------------------------------
# paymentMethods -------------------------------------------------- SECURITY NEEDED
#---------------------------------------------------- 

    @property
    def paymentMethods(self):
        return self._paymentMethods
    
    @paymentMethods.setter
    def paymentMethods(self,payMethods):
        self._paymentMethods = payMethods
        
    def addPaymentMethod(self):
        self.newPaymentMethod()
        self._paymentMethods.append(self._paymentMethod)
        
    
#----------------------------------------------------
# paymentMethod -------------------------------------------------- SECURITY NEEDED
#---------------------------------------------------- 

    @property
    def paymentMethod(self):
        return self._paymentMethod
    
    @paymentMethod.setter
    def paymentMethod(self,payMethod):
        self._paymentMethod = payMethod
        
    def newPaymentMethod(self):
        self._paymentMethod = PaymentMethod()
        
