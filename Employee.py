from User import User;

#----------------------------------------------------
# Employee Class (User Child)
#---------------------------------------------------- 

class Employee(User):
    def __init__(self):
        super().__init__()  
        self.setEmployee()

#----------------------------------------------------
# setEmployee (Sets User Permissions as Employee)
#---------------------------------------------------- 

    def setEmployee(self):
        self.setPermissions(1) 
