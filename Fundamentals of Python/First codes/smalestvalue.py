list_1=[]
n=int(input('Enter the values into List:'))
print('Enter the Values one by one::')
for i in range(0,n):
    i=int(input('Enter value ::'))
    list_1.append(i);
'''for j in range(0,n-2):
    if(list_1[j]>list_1[j+1]):
        min_1=list_1[j+1]
    else:
        min_1=list_1[j]
print(min_1)'''

print("\nThe smallest value::",min(list_1))
print("Largest value is::",max(list_1))
