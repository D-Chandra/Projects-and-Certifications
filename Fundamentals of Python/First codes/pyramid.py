#This program will make a pyramid of Numbers
num=int(input('Enter the Number till you want to print the Pyramid::'))
for i in range(1,num+1):
    print("\n")
    for j in range(num-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    if(i>1):
        for m in range(i-1,0,-1):
            print(m,end="")
    for z in range(num-i):
        print(" ",end="")
