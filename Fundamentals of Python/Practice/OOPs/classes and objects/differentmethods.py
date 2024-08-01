#instance Methods - Accessor(Get) and Mutators(Set) (Self in first argument)
#class Methods - (cls in First argument) @classmethod decorator
#static Methods - @staticmethods as decorator (pass no argument) - Use when Do a work that not inlclude work with main class variable or instance variable (For ex - Work with different Class Objects)
class prod_fan:
    BaseCompany = "HARMAN Industries"
    def __init__(self):
        self.Model = "ModelNO"
        self.Rpm = "RatePerMinute"
        self.BladeDiameter = "DiameterOfBlade"
        self.Lightfacility = "LightFacilityYesorNo"
        self.RemoteControl = "RemoteControlYesorNo"
        # print(id(self.Model)) #print object location it wil be same throughout the class
    def get_Model(self):   #Called Getter Method/Accessor (Instance Method type) Using Get is Just Convention
        # print(id(self.Model))
        print(self.Model)
    def set_Model(self,model):
        self.Model=model
    def set_Remotecontrol(self,RemoteControl): #called Setter Method/Mutator (Instance Method Type) Using Set is just convention
        self.RemoteControl = RemoteControl
    @classmethod
    def company(cls):
        print(cls.BaseCompany)
    @staticmethod
    def info():
        print("This Is the Harman Fan Class")

product = prod_fan()
# product.get_Model()
prod_fan.company() # we can also use product.company() to as here we don't need to pass object name as argument because its an class method


