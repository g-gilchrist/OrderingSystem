from Account import Account

#----------------------------------------------------
# User Class
#----------------------------------------------------        

class User(Account):      
    def __init__(self):
        self._username = None
        self._password = None
        self._permissions = None
        
        self._account = Account()
        self._role = ['Customer', 'Employee', 'Admin']        
        
#----------------------------------------------------
# username
#----------------------------------------------------    

    @property
    def username(self):
        try:
            return self._username
        except:
            return 'Error: Username does not exist.'
            
    @username.setter
    def username(self,username):   
        if len(username) > 15:
            return 'Error: Username can not be greater than 15 charachters.'
        else:        
            self._username =  str(username)    
    
#----------------------------------------------------
# password
#----------------------------------------------------    

    @property
    def password(self):
        try:
            return self._password    
        except:
            return 'Error: Password does not exist.'
        
    @password.setter
    def password(self,password):
        accepted=True
        if len(password) < 12 or len(password) > 25:
            print('Error: Passwords must be greater than 12 charachters and less than 25.')
            accepted = False
            
        if any(char.isupper() for char in password):      
            pass
        else:
            print('Error: Passwords must contain a capital letter.')
            accepted = False
            
        if any(char in ['!','@','#','$','&'] for char in password):
            pass
        else:
            print ('Error: Passwords must contain a symbol (!,@,#,$,&).')
            accepted = False
            
        if any(char in ['=','+','-','*','?','<','>',',','/',';','`','~','{','}','[',']','(',')'] for char in str(password)):
            print ('Error: Passwords may only contain the following symbols (!,@,#,$,&).')
            accepted = False
        else:
            pass
            
        if accepted is True:        
            self._password = str(password)
        else:
            return
                   
#----------------------------------------------------
# permissions
#----------------------------------------------------           
    @property
    def permissions(self):
        try:
            return self._permissions
        except:
            return False
   
    def setPermissions(self,i):
        try:
            self._permissions = self._role[int(i)]       
        except:
            return 'Error: Numbers only'
            
            
#----------------------------------------------------
# new account
#----------------------------------------------------       
            
    @property
    def account(self):
        return self._account
        
    def addAccount(self, account):
        self._account = account

#----------------------------------------------------
# delete user
#----------------------------------------------------

    def __del__(self):
        return 'User Deleted'
    


