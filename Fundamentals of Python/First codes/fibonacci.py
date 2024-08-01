num=int(input("Enter the Number till how much to how much iteration for printing Fibonacci series::"))
a=int(0)
b=int(1)
print(a,b,end=" ")
for i in range(0,num):
    c=a+b
    print(c,end=" ")
    a = b
    b = c
