#from Renter import Renter

class Renter:
    def __init__(self,nameIn,roomNumIn,daysStayingIn):
        self.name= nameIn
        self.roomNum= roomNumIn
        self.daysStaying= daysStayingIn

class LongTermRenter(Renter):
    def __init__(self,nameIn,roomNumIn,daysStayingIn,insuranceIn):
        super().__init__(nameIn,roomNumIn,daysStayingIn)

        self.insurance= insuranceIn


