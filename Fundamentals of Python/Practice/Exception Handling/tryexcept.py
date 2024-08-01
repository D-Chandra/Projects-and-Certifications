try:
    a = int(input("Enter numerator::"))
    b = int(input("Enter Denominator::"))

    print("The Division::",a/b)
    fileptr = open("..\\File handling\\Files\\filemodes.txt","r")
    strng = fileptr.read()
    print("Value Inside File is at Index 3::",strng[0:4])
except IndexError as Inerro:

    print("Error Occured::",Inerro)

except FileNotFoundError as ferro:
    print("Error Occured",ferro)

except ZeroDivisionError as zerro:
    print("Error Occured::",zerro)

except IndentationError as Inderro:
    print("Error Occured::",Inderro)

else:
    print("Program Successfully Executed::NO Exception Caught")
