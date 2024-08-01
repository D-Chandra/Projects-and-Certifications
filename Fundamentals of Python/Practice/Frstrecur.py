def bin(n):
    if n>1:
        bin(n//2)
        print(n%2,end = " ")
    else:
        print(1,end=" ")

a=int(input("Enter an integeral we will convert it to binary::"))
bin(a)
