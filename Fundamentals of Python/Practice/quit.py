#using continue and break
list_1=[]
sum=0
pro=1
while True:
    n=input("Enter value::")
    if(n=='q' or n=='Q'):
        break
    else:
        n=int(n)
        list_1.append(n)
for i in range(len(list_1)):
    sum=sum+list_1[i]
    pro=pro*list_1[i]

avg=int(sum/len(list_1))
print("The avg is::",avg)
print("The product is::",pro)
