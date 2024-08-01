
#---------------------------OBJECT location Pointers-----------------------
a = [1,2,3]    # in example of int object even assigning b separatly results in pointing to same location in memory
# b = a        # b = a  #a and b have the same contents, and are the same object
# b = [1,2,3]  # But in list its just oppposite
               # a and c have the same contents, but are two different objects at different memory addresses
b = [1,2,3,4]  # If we add another object to c, it's now got different contents to a, as well as being a different object at a different memory address

if a == b:
    print(True)
else:
    print(False)
if a is b:
    print(True)
else:
    print(False)

# b = b+40 #this aasignment changes the address of the b var (or even if you assign different type object its changes its address)
print(id(a),a)
print(id(b),b)
# data = 'diwanshu'
# data2 = list(data)
# print(data[2])
# for i in range(len(data2)):
#     if data2[i] == 'a':
#         # b=i
#         # b='A'
#         data2[i]=data2[i].upper()
#         # print(i)
# print(data2)
#-------------------------getting two sepearate locations from inbuilt copy()----------------------------------
# a = [1, 2, 3]
# b = list.copy(a) #if u do b=a then b is having the same address as a is pointing earlier
# b[0]=5
# print(id(a),a)
# print(id(b),b)