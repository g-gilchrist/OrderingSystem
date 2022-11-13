from Requirement import Requirement
from Product import Product

from datetime import datetime

#----------------------------------------------------
# Coupon Class
#----------------------------------------------------   
class Coupon():
    def __init__(self):
        self._title = None
        self._description = None
        self._discount = None
        self._expDate = None
        self._requirements = list()
        self._requirement = None
      
#----------------------------------------------------
# title
#----------------------------------------------------   
      
    @property
    def title(self):
        try: 
          return self._title
        except:
          return 'Error: title not found'
        
    @title.setter
    def title(self,title):
        self._title = title
      
#----------------------------------------------------
# description
#----------------------------------------------------   
      
    @property
    def description(self):
        try:
            return self._description
        except:
            return 'Error: description not found'
        
    @description.setter
    def description(self, description):
        self._description = description
           
#----------------------------------------------------
# discount
#----------------------------------------------------         
      
    @property
    def discount(self):
        try:
            return self._discount
        except:
            return 'Error: Discount not applied'
       
    @discount.setter
    def discount(self, discount):
        self._discount = discount
      
#----------------------------------------------------
# expiration date
#----------------------------------------------------         
      
    @property
    def expDate(self):
        try:
            return self._expDate
        except:
            return 'Error: discount expired'
        
    @expDate.setter
    def expDate(self, expDate):
        expMonth, expDay, expYear, = [int(x) for x in expDate.split('/')] 
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year 
    
        if expYear < currentYear:
            return 'Error: Coupon is expired'
        elif expYear == currentYear and expMonth < currentMonth:
            return 'Error: Coupon is expired'
        elif expYear == currentYear and expMonth == currentMonth and expDay < currentDay:
            return 'Error: Coupon is expired'
        else: 
            self._expDate = expDate

#----------------------------------------------------
# requirements
#----------------------------------------------------   
      
    @property
    def requirements(self):
        try:
            return self._requirements
        except:
            return 'Error: No requirements set'
       
    @requirements.setter
    def requirements(self, requirements):
        self._requirements = requirements 
      
    def addRequirement(self):
        self.newRequirement()
        self._requirements.append(self._requirement) 
        
#----------------------------------------------------
# requirements
#----------------------------------------------------   
      
    @property
    def requirement(self):
        try:
            return self._requirement
        except:
            return 'Error: Requirement not set'
        
    @requirement.setter
    def requirement(self, requirement):
        self._requirement = requirement 
    
    def newRequirement(self):
        self._requirement = Requirement()
        
#----------------------------------------------------
# repr
#----------------------------------------------------  

    def __repr__(self):
        return f'{self._title}, {self._description}, ${self._discount:.2f}, {self._expDate}, {self._requirements}'

#----------------------------------------------------
# str
#----------------------------------------------------  

    def __str__(self):
        return f'{self._title}, {self._description}, ${self._discount:.2f}, {self._expDate}, {self._requirements}'

#----------------------------------------------------
# delete coupon
#----------------------------------------------------    
    def __del__(self):
        return 'Coupon Deleted'
