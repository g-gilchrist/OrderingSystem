#----------------------------------------------------
# Product Class
#----------------------------------------------------   
class Product:
    def __init__(self):
        self._categories = ['Pizza','Sides','Salads','Deserts','Beverage']
        self._category = None
        self._title = None
        self._imgSrc = None
        self._description = None
        self._price = None
        
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
        
    def delSize(self,idx):
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
# title
#----------------------------------------------------    
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = str(title)
        
#----------------------------------------------------
# image source
#----------------------------------------------------   
       
    @property
    def imgSrc(self):         
        return self._imgSrc
    
    @imgSrc.setter                    
    def imgSrc(self, imgSrc):
        self._imgSrc = str(imgSrc)
        
#----------------------------------------------------
# description
#----------------------------------------------------  
            
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self,description):
        self._description = str(description)
        
#----------------------------------------------------
# price
#----------------------------------------------------
        
    @property
    def price(self):
        return self._price    
    
    @price.setter
    def price(self, price):
        try:
            self._price=float(price)
        except:
            return'Error: Invalid input, numbers only.'
            
#----------------------------------------------------
# repr
#----------------------------------------------------      
           
    def __repr__(self):
        return f'{self.category}, {self.title}, {self.imgSrc}, {self.description}, ${self.price:.2f}'
    
#----------------------------------------------------
# str
#----------------------------------------------------       
    
    def __str__(self):
        return f'{self.category}, {self.title}, {self.imgSrc}, {self.description}, ${self.price:.2f}'
    
#----------------------------------------------------
# del
#----------------------------------------------------  

    def __del__(self):
        return 'Product Deleted'    

    