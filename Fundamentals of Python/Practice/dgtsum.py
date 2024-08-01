value=int(input("Enter a number::"))
i=0
sum=0
fetch=0
reverse=0
while (value!=0):
    fetch=value%10
    sum=sum+fetch
    reverse=(reverse*10)+fetch
    value=value//10
print(sum)
print(reverse)
