data = input("Enter the values in the list with spaces between two values::").split(" ")
for i in data:
    x = data.count(i)
    print(x)
    if x>1:
        print(False)
        exit()
    else:
        pass
print(True) 
    