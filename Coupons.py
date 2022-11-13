from Coupon import Coupon

#----------------------------------------------------
# Coupons Class
#----------------------------------------------------   
class Coupons():
    def __init__(self):
        self._coupon = None
        self._coupons = list()

#----------------------------------------------------
# coupons
#----------------------------------------------------   

    @property
    def coupons(self):
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        self._coupons = coupons

    def addCoupon(self):
        self.newCoupon()
        self._coupons.append(self._coupon)

    def removeCoupon(self, title):
        for idx, coup in enumerate(self._coupons):
            if(coup._title == title):
                self._coupons.pop(idx)
                
#----------------------------------------------------
# coupon
#----------------------------------------------------

    @property
    def coupon(self):
        return self._coupon

    @coupon.setter
    def coupon(self, coupon):
        self._coupon = coupon

    def newCoupon(self):
        self._coupon = Coupon()
        
        
