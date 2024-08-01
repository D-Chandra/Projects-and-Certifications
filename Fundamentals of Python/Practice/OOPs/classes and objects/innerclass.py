class Asus:
    def __init__(self):
        self.brandName = "Asus"
        self.lap = self.Laptops()
    class Laptops:   # an Inner class
        def specs(self):
            self.cpu = "i5 8250u"
            self.ram = "16gb ddr4"
            self.gpu = "Mx150"
            self.cateogry = "Ultrabook"
        def changespecs(self):
            self.gpu = input("Enter the New gpu name::")
            
    def show(self):
        print(self.brandName)
        print(self.lap.cpu)
        print(self.lap.ram)
        print(self.lap.gpu)
        print(self.lap.cateogry)

#creating object of innerclass
brand1 = Asus()
lap1 = Asus.Laptops() # Because inside Asus class so can be directly constructed as we are calling constructor of class Laptops 
lap2 = brand1.lap # as we have defined a variable in init method named 'lap' which holds a poniter to an object of Laptops 
                  # now lap2 is new object pointer of Class Laptops
print(id(lap1))
print(id(lap2))   # we can see id of both objects
print(id(brand1))
print(brand1.brandName)
brand1.lap.specs() # these three lines must be called before calling any variable of Laptops() class as variables are still not in memory
lap1.specs()
lap2.specs()
print(brand1.lap.cpu) # different ways we can access the variables and methods of Inner class
print(lap1.gpu)
print(lap2.ram)

