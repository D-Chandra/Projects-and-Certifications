lst=[]
n=int(input("Enter how much values u want to enter::"))
for i in range(0,n):
    lst.append(int(input("Enter value::")))

#print(lst[])
num=int(input("Enter the value u want to remove::"))
'''lst1=[]
for i in range(0,n):
    #print(lst[i])
    if(lst[i]==num):
        continue
    else:
        lst1.append(lst[i])'''

for i in range(0,n):
    lst.remove(num)

print(lst)
