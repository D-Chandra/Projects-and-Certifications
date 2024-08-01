# '''
# thisList = ["Apple", "Banana", "Cherry"]
# thisList.insert(1,"Orange")
# thisList.remove()
# print(thisList)
# '''
# '''
# L1 = [0,1,2,4,6,7]
# for i in range(0,10):
#     if i not in L1:
#         L1.insert(i,i)
    
# print(L1)
# '''
# '''
# exList = [0,1,2,3,4,4,5,6]
# exList.pop()
# print(exList)
# '''
# '''
# thisList = ["Apple", "Banana", "Cherry"]
# print(thisList)
# thisList.clear(); print(thisList)
# del thisList; print(thisList)
# '''
# '''
# thisList = ["Apple", "Banana", "Cherry"]
# myList = thisList.copy(); print("Using copy() : ",myList)
# myList = list(thisList); print("Using list constructor: ",myList)
# '''
# '''
# listF = ["apple","banana","orange"]
# listV = ["brinjal","carrot","onion"]
# #list3 = listF + listV; print("Using concatination operator: ",list3)

# #for i in listF:
# #    listV.append(i)
# #print("Append method: ",listV)

# listF.extend(listV); print(listF)
# listV.extend(listF); print(listV)
# '''
# '''
# string1 = "Fruits: Banana Apple Orange,Vegetables: Brinjal Potato Onion"
# LIST = string1.split(',')
# fruit = LIST[0]
# veg = LIST[1]
# print(fruit,"\n",veg)

# string1 = "Fruits: Banana Apple Orange,Vegetables: Brinjal Potato Onion"
# string2=string1.replace(':',' ')
# print(string2)
# '''

# '''
# string1 = input("Enter a string: ")
# chkWrd = ["light","on"]
# if both(["light","on"] in string1):
# 	print("On and light are present in the entered string !")
# else:
# 	print("Either On or light are present in the entered string !")
# '''
# '''
# age = 45
# print("My age is: {}".format(age))



# thisTuple = ("apple","banana","cherry")
# for x in thisTuple:
# 	print(x)


# thisDict = {
# 	"brand":"ford",
# 	"model":"mustang",
# 	"year" : 1964
# }
# #print(thisDict['model'])
# #print(thisDict.get('brand'))
# for x, y in thisDict.items():
# 	print(x, y)
	
# #thisDict['year'] = 2020
# #print(thisDict['year'])


# str1 = input("Enter your string: ")
# if "on" and "light" in str1 :
# 	print("Turning on the light")
# else:
# 	print("Turning off the light")




# thisDict = {
# 	"brand":"ford",
# 	"model":"mustang",
# 	"year" : 1964
# }

# newDict = thisDict.copy()

# for x in newDict.values():
# 	print(x)




# for x, y in thisDict.items():
# 	print(x, y)
# print("\n\n")
# for x in thisDict:
# 	print(x)
# print("\n\n")
# print(thisDict['model'])
# print(thisDict.get('brand'))
# thisDict['year'] = 2020
# print(thisDict['year'])


# child1 = {
# 	"Name":"Elliot",
# 	"Year":2000
# }

# child2 = {
# 	"Name":"Tobais",
# 	"Year": 2007
# }

# child3 = {
# 	"Name":"Linus",
# 	"Year":2011
# }

# myFamily = {
# 	"Child1" : child1,
# 	"Child2" : child2,
# 	"Child3" : child3
# }

# for k,v in myFamily.items():
# 	for i,j in v.items():
# 		print(k," --> ",i,j,end = "")

# import pyfirmata
# import time

# board = pyfirmata.Arduino('COM2')
# anPin = board.get_pin('a:6:i')
# it = pyfirmata.util.Iterator(board)

# it.start()
# anPin.enable_reporting()
# while True:
# 	readIng = anPin.read()
# 	if readIng != None:
# 		volt = readIng*5.0
# 		print("Reading=%f\tVoltage=%f" %(reading, volt))
# 		time.sleep(1)



# import pyfirmata
# from pyfirmata import INPUT, OUTPUT, PWM, SERVO
# import time

# pin= 10
# board = pyfirmata.Arduino('COM4')
# serv=board.get_pin('d:10:p')
# board.digital[pin].mode = SERVO

# while True:
#     angle=input("Enter the angle to rotate Servo Motor from 0 to 180: ")
#     #servo.write(int(angle))
#     board.digital[13].write(angle)
#     time.sleep(1) # delays for 5 seconds


# '''
# class xvy:
# 	def
# import csv
# with open("persons.csv",'w',newline='') as csvfile:
# 	filewriter = csv.writer(csvfile, delimiter=',')
# 	filewriter.writerrow(['Name','Age','Profession'])
# 	filewriter.writerrow(['Derek','23','Docter'])
# 	filewriter.writerrow(['Ni Pinping','68','Secratory'])
# 	filewriter.writerrow(['Chadra','21','Sweeper'])

# with open('persons1.csv', 'w', newline='') as csvfile:
#     filewriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     filewriter.writerow(['Name', 'age','Profession'])
#     filewriter.writerow(['Derek','23', 'Doctor'])
#     filewriter.writerow(['Steve', '22','Engineer'])
#     filewriter.writerow(['Paul', '32', 'Manager'])
# row_list = [["SN", "Name", "Contribution"],
#              [1, "Linus Torvalds", "Linux Kernel"],
#              [2, "Tim Berners-Lee", "World Wide Web"],
#              [3, "Guido van Rossum", "Python Programming"]]
# with open('protagonist.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(row_list)

# with open('players.csv','w',newline='') as file:
# 	fieldnames = ['player_name','fide_rating']
# 	writer = csv.DictWriter(file,fieldnames=fieldnames)
# 	writer.writeheader()
# 	writer.writerow({'player_name':'Magnus Carlsen','fide_rating':2870})
# 	writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating':2822})
# 	writer.writerow({'player_name':'Ding Liren','fide_rating:2801':2801})
	
# import csv
# with open 
