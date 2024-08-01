val = input("Enter a string::")
if val == val[::-1]:
    fileptr = open("Files\\palincheck.txt","w")
    lst = [val+"\n",val+"\n",val+"\n",val+"\n",val+"\n"]
    # lst = list((val*5).split("\n"))
    print("String Is palindrome")
    fileptr.writelines(lst)
    fileptr.close()
else:
    print("SORRY not a palindrome")

