def erromsg():
    print("heelo world")

class ConversionError(Exception):
    def erromsg(self):
        print("Conversion Error Occured")
    # def __init__(self,msg=("Error in explicit Conversion")):
    #     self.msg = msg
    #     super().__init__(self.msg)

a = input("Enter a Value::")
try:
    print("Type of value Entered::",type(a))
    a = int(float(a))
    if a==False:
        raise ConversionError("An Error Occured During Conversion")
    print("After Conversion to Integer Type::",type(a))
    # try:
    #     a = int(float(a))
    #     print("After Conversion to Integer Type::",type(a))
    # except ValueError as Ve:
    #     print("An Error (Inside Block) Occured::",Ve)  
# except Exception as Ex:
#     print("An Error(Outside Block) Occured::",Ex)
except ConversionError as Ce:
    print("An Error(Outside BLock) Occurred::",Ce)
# except ValueError as ind:
#     print("An Error(Outside Block) Occured::",ind) //Already using a base class so no need to use inherited childs
else:
    print("Programe Executed without exceptions Successfully")

