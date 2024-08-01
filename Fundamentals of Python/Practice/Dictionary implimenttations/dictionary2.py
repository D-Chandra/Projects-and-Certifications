k1=int(float(input("Enter The Amount Of Keys u want to Enter::")))
key=0
dctnry = {}
# dctnry=dict((key=int(float(input("Enter A Key::"))) dctnrytry[key]=input("Enter Its Relative Value::")) for i in range(0,k1))
for i in range(0,k1):
    key=input("Enter A Key::")
    dctnry[key]=input("Enter Its Relative Value::")

print(dctnry)

deltvar = input("Enter Key U want to delete::")
del dctnry[deltvar]

fuldel = input("Enter \"1\" if u want clear \"0\" if you dont")

def dictdel():
    dctnry.clear()
    print("Dictionary cleared",dctnry)
    

def nodictdel():
    print("Dictionary not Deleted",dctnry)

dictdel() if (fuldel=='1') else nodictdel()
# for i in range(0,k1):

# print(type(dctnry))
# print(dctnry)
