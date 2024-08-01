try:
    fileptr = open("Files//india.txt","r")
    data = fileptr.read()
    vowellower = set("aeiou")
    vowelupper = set("AEIOU")
    lst1 = list()
    for i in data:
        if i in vowellower:
            lst1.append(i.upper())
            # print(i)
        elif i in vowelupper:
            lst1.append(i.lower())
        else:
            lst1.append(i)
    print(lst1)
    fileptr.close
    fileptr = open("Files//india.txt","w")
    fileptr.writelines(lst1)
    fileptr.close
except Exception as e:
    print(e)