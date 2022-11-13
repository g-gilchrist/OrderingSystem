
#----------------------------------------------------
# Account Class
#----------------------------------------------------    

class Account():
    def __init__(self):
        self._firstName = None
        self._lastName = None
        self._email = None
        self._phoneNum = None
        self._address = None
        self._city = None
        self._state = None
        self._zipCode = None

#----------------------------------------------------
# first name
#----------------------------------------------------  

    @property
    def firstName(self):
        return self._firstName
    
    @firstName.setter
    def firstName(self, firstName):
        firstName = firstName.strip()
        if len(str(firstName)) < 2 or len(str(firstName)) > 50:
            return 'Error: Please enter valid name.'

        if not firstName.isalpha():
            return 'Error: Name must be letters'
        else:
            self._firstName = str(firstName)
        
#----------------------------------------------------
# last name
#----------------------------------------------------          
        
    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter
    def lastName(self, lastName):
        lastName = lastName.strip()
        if len(str(lastName)) < 2 or len(str(lastName)) > 50:
            return 'Error: Please enter valid name.'

        if not lastName.isalpha():
            return 'Error: Name must be letters'
        else:
            self._lastName = str(lastName)
        self._lastName = str(lastName)
        
#----------------------------------------------------
# email
#----------------------------------------------------  

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = str(email)

#----------------------------------------------------
# phone number
#----------------------------------------------------  

    @property
    def phoneNum(self):
        return self._phoneNum
    
    @phoneNum.setter
    def phoneNum(self, phoneNum):
        self._phoneNum = int(phoneNum)
        
# -------------------------------------------------------------------------------------------#
#                                        address                                             #
# -------------------------------------------------------------------------------------------#

    @property
    def address(self):
        try:
            return self._address
        except:
            return 'Address is invalid.'

    @address.setter
    def address(self, address):
       accepted = True

       if len(address) < 1 or len(address) > 30:
           return 'Street address should be between 1 and 50 characters.'
           accepted = False

       if any(char in ['=', '+', '-', '*', '?', '<', '>', ',', '/', ';', '`', '~', '{', '}', '[', ']', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')'] for char in
              str(address)):
           return 'Error: Address should not contain symbols.'
           accepted = False

       if accepted is True:
           self._address = str(address)


# -------------------------------------------------------------------------------------------#
#                                            city                                            #
# -------------------------------------------------------------------------------------------#

    @property
    def city(self):
        try:
            return self._city
        except:
            return 'Invalid City.'

    @city.setter
    def city(self, city):
        accepted = True

        if len(city) < 1 or len(city) > 17:
            return 'City should be no more than 17 characters long, or no less than 1 character in length.'
            accepted = False

        if any(char in ['=', '+', '-', '*', '?', '<', '>', ',', '/', ';', '`', '~', '{', '}', '[', ']', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.'] for char in
           str(city)):
            return 'Error: City should not contain symbols.'
            accepted = False

        if str(city).isnumeric():
            return 'Error: Zip code are numbers only'
            accepted = False

        if accepted is True:
            self._city = str(city)
        else:
            return

# -------------------------------------------------------------------------------------------#
#                                           State                                            #
# -------------------------------------------------------------------------------------------#
    @property
    def state(self):
        try:
            return self._state
        except:
            return 'Error: State not on file'

    @state.setter
    def state(self, idx):  # set
        statesList = [["AL", "Alabama"], ["AK", "Alaska"], ["AZ", "Arizona"], ["AR", "Arkansas"],
                        ["CA", "California"], ["CO", "Colorado"], ["CT", "Connecticut"], ["DC", "Washington DC"], ["DE", "Delaware"],
                        ["FL", "Florida"], ["GA", "Georgia"], ["HI", "Hawaii"], ["ID", "Idaho"], ["IL", "Illinois"], ["IN", "Indiana"],
                        ["IA", "Iowa"], ["KS", "Kansas"], ["KY", "Kentucky"], ["LA", "Louisiana"], ["ME", "Maine"], ["MD", "Maryland"], 
                        ["MA", "Massachusetts"], ["MI", "Michigan"], ["MN", "Minnesota"], ["MS", "Mississippi"], ["MO", "Missouri"],
                        ["MT", "Montana"], ["NE", "Nebraska"], ["NV", "Nevada"], ["NH", "New Hampshire"], ["NJ", "New Jersey"],
                        ["NM", "New Mexico"], ["NY", "New York"], ["NC", "North Carolina"], ["ND", "North Dakota"], ["OH", "Ohio"],
                        ["OK", "Oklahoma"], ["OR", "Oregon"], ["PA", "Pennsylvania"], ["RI", "Rhode Island"], ["SC", "South Carolina"],
                        ["SD", "South Dakota"], ["TN", "Tennessee"], ["TX", "Texas"], ["UT", "Utah"], ["VT", "Vermont"], ["VA", "Virginia"],
                        ["WA", "Washington"], ["WV", "West Virginia"], ["WI", "Wisconsin"], ["WY", "Wyoming"]]

        try:
            self._state = statesList[int(idx)]
        except:
            return 'Input needs to be a number.'

# -------------------------------------------------------------------------------------------#
#                                          zipCode                                           #
# -------------------------------------------------------------------------------------------#

    @property
    def zipCode(self):
        try:
            return self._zipCode
        except:
            return 'Error Zip code is incorrect.'

    @zipCode.setter
    def zipCode(self, zipCode):
        accepted = True

        if len(str(zipCode)) < 1 or len(str(zipCode)) > 5:
            print('Zip code should be 5 numbers in length.')
            accepted = False

        if not str(zipCode).isnumeric():
            return 'Error: Zip code are numbers only'
            accepted = False

        if any(char in ['=', '+', '-', '*', '?', '<', '>', ',', '/', ';', '`', '~', '{', '}', '[', ']', '!', '@', '#',
                        '$', '%', '^', '&', '*', '(', ')', '.'] for char in str(zipCode)):
            print('Error: City should not contain symbols.')
            accepted = False

        if accepted is True:
            self._zipCode = str(zipCode)
        else:
            return
        
#----------------------------------------------------
# repr
#----------------------------------------------------                      
    def __repr__(self):
        return f'{self.firstName} {self.lastName}, {self.email}, {self.phoneNum}, {self.address}, {self.city}, {self.state}, {self.zipCode}'
    
#----------------------------------------------------
# str
#----------------------------------------------------            
    def __str__(self):
        return f'{self.firstName} {self.lastName}, {self.email}, {self.phoneNum}, {self.address}, {self.city}, {self.state}, {self.zipCode}'
    
#----------------------------------------------------
# delete topping
#----------------------------------------------------    
    def __del__(self):
        return 'Topping Deleted'       
        
        
        
        
        
        
        
        


