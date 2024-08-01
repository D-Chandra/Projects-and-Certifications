class computer:
    __processor = 'Ryzen 5600x'
    _Gpu = 'GTX 1660ti'
    _ram = '16gb ddr4 3200'
    _storage = '256gb ssd + 1tb hardrive'
    def specifications(self):
        print("Specifications for the Compute::",self)
        print(self.__processor)
        print(self._Gpu)
        print(self._ram)
        print(self._storage)
    def update(self):
        self._ram = '24gb ddr56 pro max legend ultra 45k ghz clock'  #here the this is instance variable
        #whenever classobjectname._ram will be called this instance varaible will be mapped not the static one
    def changeprocessor(self,processor):
        self.__processor = processor
        
    
c1 = computer()  # constuctor of computer class is called
# print(c1._Gpu)
# print(c1._computer__processor,"\n")
# computer.specifications(self=c1)  # directly write here c1 arguments asking for which abject you want to call specification method (self is more like this in c++)
# computer.specifications(c1)
# c1.update()  #if you call this its passing self(or c1 in this case) in its argument by default so its going to update for c1
c1.specifications()
print(id(c1))
print(type(c1))
# addr=c1  //pointer to the class c1
# addr = addr+1
c2 = computer()
c2.specifications()
c2._Gpu = 'RTX 1660ti'
# print(addr._Gpu)
if c2._Gpu == c1._Gpu:
    print("They have same Gpu")
else:
    print("They Have different Gpu")

c2.changeprocessor(input("Enter a Processor name::"))
c2.specifications()
c3 = computer()
computer.specifications(c3) 
print(computer._Gpu) #this _Gpu is the static variable so can be called like that / c3._Gpu - will take the self._Gpu if avilable
# a = 5
print(c3._Gpu)  #its Directly printing a static variable of the class
# a.bit_length()