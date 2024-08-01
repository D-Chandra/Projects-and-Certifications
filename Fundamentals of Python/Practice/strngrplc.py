print("<----------------Hey User enter any random String Value in this Program-----------------> ")
print("<----------------Use strings which ends and not ends with 'ing' and if you want to exit the program then type exit and then press Enter ---------------------------->")
while(True):
    strng=input("GIVE YOUR STRING VALUE::")
    if(len(strng)>=3):
        if(strng[-3:]=='ing'):
            strng=strng.replace(strng[-3:],'ly')
            print("Your new String value is::",strng)
        elif(strng=='Exit' or strng=='exit' or strng=='EXIT'):
            print("<--------------Program succesfully Terminated----------------->")
            quit()
        else:
            strng=strng+'ing'
            print("Your new String value is::",strng)
    else:
        print("<---------------Your string length is less than three so you will not see any change Please re enter a new value with more >= 3 length-------------->")
        print("<--------If you want to exit the program then type exit and then press Enter------>")
