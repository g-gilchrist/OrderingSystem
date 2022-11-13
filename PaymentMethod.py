from datetime import datetime

# -------------------------------------------------------------------------------------------#
#                                 PaymentMethod Class                                        #
# -------------------------------------------------------------------------------------------#

class PaymentMethod:
    def __inti__(self):
        self._paymentName = None
        self._cardNum = None
        self._cardType = None
        self._cardExpDate = None
        self._cardCvv = None
        self._name = None
        self._address = None
        self._street = None
        self._city = None
        self._state = None
        self._zipCode = None

# -------------------------------------------------------------------------------------------#
#                                     paymentName                                            #
# -------------------------------------------------------------------------------------------#

    @property
    def paymentName(self): 
        try:
            return self._paymentName
        except:
            return 'Error: Payment name not on file.'
    
    @paymentName.setter
    def paymentName(self, paymentName):
        self._paymentName = paymentName    

# -------------------------------------------------------------------------------------------#
#                                        cardNum                                             #
# -------------------------------------------------------------------------------------------#

    @property
    def cardNum(self): 
        try:
            return self._cardNum
        except:
            return 'Error: Card Number not on file.'

    @cardNum.setter
    def cardNum(self, cardNum):
        self.cardType = cardNum

# -------------------------------------------------------------------------------------------#
#                                        cardType                                            #
# -------------------------------------------------------------------------------------------#

    @property
    def cardType(self):      
        try:
            return self._cardType
        except:
            return 'Error: Card Type not on file. '


    @cardType.setter
    def cardType(self, cardNum):

        cardMii = {
            'American Express': ['34', '37'],
            'Discover': ['6011'],
            'Mastercard': ['51', '52', '53', '54', '55'],
            'Visa': ['4']
        }

        if len(str(cardNum)) == 15 and str(cardNum)[:2] in cardMii.get('American Express'):
            self._cardType = 'American Express'
            self._cardNum = int(cardNum)

        elif str(cardNum)[:4] in cardMii.get('Discover') or str(cardNum)[:4] in cardMii.get('Discover'):
            self._cardType = 'Discover'
            self._cardNum = int(cardNum)

        elif len(str(cardNum)) == 16 and str(cardNum)[:2] in cardMii.get('Mastercard'):
            self._cardType = 'Mastercard'
            self._cardNum = int(cardNum)

        elif len(str(cardNum)) in [13, 16] and str(cardNum)[:1] in cardMii.get('Visa'):
            self._cardType = 'Visa'
            self._cardNum = int(cardNum)

        else:
            return 'Error: Invalid card number'

# -------------------------------------------------------------------------------------------#
#                                        cardExpDate                                         #
# -------------------------------------------------------------------------------------------#

    @property
    def cardExpDate(self):
        try:
            return self._cardExpDate
        except:
            return 'Error: No Experiation date on file'


    @cardExpDate.setter
    def cardExpDate(self, cardExpDate):
        expMonth, expYear = [int(x) for x in cardExpDate.split('/')]
        currentMonth = datetime.now().month
        currentYear = int(str(datetime.now().year)[2:])

        if expYear < currentYear:
            return 'Error: Card has expired.'
        elif expYear == currentYear and expMonth < currentMonth:
            return 'Error: Card has expired.'
        else:
            self._cardExpDate = cardExpDate

# -------------------------------------------------------------------------------------------#
#                                        cardCvv                                             #
# -------------------------------------------------------------------------------------------#

    @property
    def cardCvv(self):
        try:
            return self._cardCvv
        except:
            return 'Error: Card Cvv is invalid'

    @cardCvv.setter
    def cardCvv(self, cardCvv):
        try:
            if len(str(cardCvv)) in [3, 4]:
                self._cardCvv = int(cardCvv)
            else:
                return 'Error: Cvv is invalid.'
        except:
            return 'Error: numerical values only'

# -------------------------------------------------------------------------------------------#
#                                        name                                                #
# -------------------------------------------------------------------------------------------#

    @property
    def name(self):
        try:
            return self._name
        except:
            return 'Error: No name on file' 

    @name.setter
    def name(self, name):
        name = name.strip()
        if len(str(name)) < 2 or len(str(name)) > 50:
            return 'Error: Please enter valid name.'

        try:
            firstName, lastName = [str(x) for x in name.split(' ')]
        except:
            return 'Error: First and Last name must be entered'

        if not firstName.isalpha() or not lastName.isalpha():
            return 'Error: Name must be letters'
        else:
            self._name = str(name)

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

       if len(address) < 5 or len(address) > 30:
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
            return 'Error: cities are letters only'
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

# -------------------------------------------------------------------------=---------------------#
#                                           repr                                                 #
# -------------------------------------------------------------------------=---------------------#

    def __repr__(self):
        return f'{self._cardNum}, {self._cardExpDate}, {self._cardCvv}, {self._name}, {self._address}, {self._city}, {self._state}, {self._zipCode}'

# ---------------------------------------------------------------------=-------------------------#
#                                           str                                                  #
# ------------------------------------------------------------------------=----------------------#
    def __str__(self):
        return f'{self._cardNum}, {self._cardExpDate}, {self._cardCvv}, {self._name}, {self._address}, {self._city}, {self._state}, {self._zipCode}'

# -------------------------------------------------------------------------------------------#
#                                  delete PaymentMethod                                      #
# -------------------------------------------------------------------------------------------#
    def __del__(self):
        return 'User Deleted'






