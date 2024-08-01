x=float(input("Enter the Amount Of the Bill::"))
if x<100 and x>=0:
    print("Chargeable amount will be :: RS 5.95 per unit")
elif x>100:
    print("Chargeable amount will be :: RS 6.95 per unit")
else:
    print("The input value is invalid")
