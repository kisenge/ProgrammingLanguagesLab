class Cat:
    def __init__(self,nameIn,weightIn,colourIn):
        self.name= nameIn
        self.weight= weightIn
        self.colour= colourIn


    def to_string(self):
        print(self.name +"("+self.colour+"): ", self.weight, "lbs")