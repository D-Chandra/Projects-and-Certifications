try:
    fileptr = open("Files//Personalfile.txt","r")
    data = fileptr.read()
    # vowellower = set("aeiou")
    # vowelupper = set("AEIOU")
    lst1 = list()
    for i in data:
        if i == 'a' or i == 'A':
            lst1.append('APPLE')
            # print(i)
        # elif i in vowelupper:
        #     lst1.append(i.lower())
        elif i == 'e' or i == 'E':
            lst1.append('EYE')
        elif i == 'i' or i == 'I':
            lst1.append('INDIA')
        elif i == 'o' or i == 'O':
            lst1.append('OCTOBER')
        elif i == 'u' or i == 'U':
            lst1.append('UNIVERSITY')
        else:
            lst1.append(i)
    print(lst1)
    fileptr.close
    fileptr = open("Files//Personalfile.txt","w")
    fileptr.writelines(lst1)
    fileptr.close
except Exception as e:
    print(e)