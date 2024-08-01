#-------------None Object--------------------#
# print(type(print('Hello')))
# i=None
# print(type(i))
# def random():
#     pass
# print(random())
#-------------Normal Function-----------------#
# def primeornot(a): #what is flag variable; == count ;
#     a = int(a)
#     count = 0
#     for i in range(2,a):
#         if a%i==0:
#             count += 1
#     if count == 0:
#         print("Prime no",a)
#     else:
#         print("NOt a Prime",a)

# a = input("Enter a Value::")
# primeornot(a)

#-----------required+keyword args--------------#
# def defaultfun(d,a=10,b=20):
#     print(a+b+d)

# defaultfun(67,a=20,b=50)
#-------------Varaible length------------------#
# def varargs(*args):
#     args2 = list(args)
#     for i in range(len(args2)):
#         if args2[i]%2!=0:
#             args2[i]=(args2[i])**2

#     args2 = tuple(args2)   
#     print(args2)
            
            
# varargs(6,9,25,8,10,129,4)
#-------------Multiple keyword arguments--------#
# def mulplekwdargs(random):
#     for i in random:
#         print(i,random[i])    # returns dictionry 
    #print(random.keys(),random.values())
# val =input("Enter values in like(key=value(space)::").split(" ")
# val = dict(val) 
# lis1 = [1,2,3,'hello',4,5,'world']
# dic2 = {i:lis1[i] for i in range(len(lis1))} 
# print(val)
# print(type(lis1),"::",lis1)
# print(type(dic2),"::",dic2)
# mulplekwdargs(val)
# lis1 = lst.apppend[i] for i in range(0,6)  
# lis1[i] for i in range(len(lis1))
#-------------------------#
        