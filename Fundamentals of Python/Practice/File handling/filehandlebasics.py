fileptr = open("Files\\Address.txt","r")
if fileptr:
    print("File creation successful")
    # val=list(input("Enter The String with Spaces here::").split(" "))
    #val = 'Lovely Professional University,\nJalandhar :- DELHI Gt Road,\nPhagwara,Punjab(India)-144411.'
    val= list(fileptr.readline().split(" "))
    print(val)
    fileptr.close()
    fileptr1 = open("Files\\Address.txt","w")
    for i in val:
        fileptr1.write(i+"\n")
    fileptr1.close()
else:
    print("file Creation Error")