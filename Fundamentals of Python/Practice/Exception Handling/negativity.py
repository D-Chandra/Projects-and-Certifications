class NegativeDistanceError(Exception):
    def __init__(self,msg="Negative Distance Entered"):
        self.msg = msg
        super().__init__(self.msg)
try:
    a = int(input("Enter M Distance::"))
    b = int(input("Enter N Distance::"))
    if(a<0 or b<0):
        raise NegativeDistanceError
    print("Distance Diff::",abs(a-b))
except NegativeDistanceError as n:
    print(n)
else:
    print("Program Executed Successfully")
