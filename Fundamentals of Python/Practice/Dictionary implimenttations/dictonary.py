dctnry ={}  #empty dictionary
print(type(dctnry))

lst=[[1,"Diwanshu"],[2,"Chandra"],[3,"Hello"]]
print(type(lst))
print(lst)
dctnry = dict(lst)
print(type(dctnry))
print(dctnry)
print(dctnry[1])
dctnry[1]="Diyanshu"
print(dctnry.keys())
dctnry[4]="World"
dctnry[5]=dict( [["1 2 3 4" ,"diwanshu"] ,["ki jay jay kaar","random string"]] )
print(dctnry[5]["ki jay jay kaar"][3])
# print(type(dctnry))
# print(dctnry[5])
# lst1=list(dctnry.values())
# print(type(lst1))
# print(lst1[4])
# dctnry2=dict(lst1[4])
# print(type(dctnry2))
# print(dctnry2["ki jay jay kaar"][3])
# print(dctnry.values())
