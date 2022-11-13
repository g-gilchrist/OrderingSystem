from User import User;

#----------------------------------------------------
# Admin Class (User Child)
#---------------------------------------------------- 

class Admin(User):
    def __init__(self):
        super().__init__()
        self.setAdmin()
        
#----------------------------------------------------
# setAdmin (Sets User Permissions as Admin)
#---------------------------------------------------- 
            
    def setAdmin(self):
        self.setPermissions(2) 
