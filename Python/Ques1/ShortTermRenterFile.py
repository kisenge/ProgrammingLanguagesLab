#from Renter import Renter

class Renter:
    def __init__(self,nameIn,roomNumIn,daysStayingIn):
        self.name= nameIn
        self.roomNum= roomNumIn
        self.daysStaying= daysStayingIn

class ShortTermRenter(Renter):
    def __init__(self, nameIn, roomNumIn, daysStayingIn, breakfastIn):
        super().__init__(nameIn, roomNumIn, daysStayingIn)

        self.breakfast = breakfastIn