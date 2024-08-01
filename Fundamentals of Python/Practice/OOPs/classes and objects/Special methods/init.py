class computer:
    # _processor = 'For ex-Ryzen 5600x'
    # _Gpu = 'For ex-GTX 1660ti'
    # _ram = 'For ex-16gb gddr4 3200'
    # _storage = 'For ex-256gb ssd + 1tb hardrive'
    def __init__(self):  # Its Same ad constructors in c++  # init means initialize (initialize variables)
                         # print("In the Init Function")
                         # We can also take values as argument assign it self (ex-self._Gpu = gpu)
        self._processor = "No Processor Defined"
        self._Gpu = "No Gpu Defined"
        self._ram = "No Ram Selected"
        self._storage = "No Storage type selected"
        print(self._processor)
        print(self._Gpu)
        print(self._ram)
        print(self._storage) 
    
    def specifications(self):
        self._processor = input("Enter a Processor Name::"+"\'For ex-Ryzen 5600x\'==")
        self._Gpu = input("Enter a Gpu Name::"+"\'For ex-GTX 1660ti\'==")
        self._ram = input("Enter Ram Config::"+"\'For ex-16gb gddr4 3200\'==")
        self._storage = input("Enter a Storage device Name::"+"\'For ex-256gb ssd + 1tb hardrive\'==")
    def display(self):
        print("\n",self._processor)
        print(self._Gpu)
        print(self._ram)
        print(self._storage) 
    

c1 = computer()  #init function will get automatically called as constructor
# print(c1._processor)
c1.specifications()
c1.display()
# computer.specifications(c2)


