#This programs Tests and explains the instance and static vriables in a class
#Namespace = Area where You create and store the object variable(Class Namspace = class variables(static variables) are stored and Object/Insatnce namespace = object and instance variables are stored)
class _6e:
    number_of_students = 64
    name = 'NameOfStudent'
    roll_no = 'RollNumberofStudent'
    uni_id = 'UniversityIdOfStudent'
    contact_no = 'ContactNoOfStudent'
    def __init__(self):
        #random = 56 #this variable just belongs to __init__ neither can be called with classname or objectname
        self.name = 'NameOfStudent'
        self.roll_no = 'RollNumberofStudent'
        self.uni_id = 'UniversityIdOfStudent'
        self.contact_no = 'ContactNoOfStudent'
    def registerStudent(self,name,roll_no,uni_id,contact_no):
        #random = 90 #same here only for registerStudent
        self.name = name
        self.roll_no = roll_no
        self.uni_id=uni_id
        self.contact_no=contact_no
        self.number_of_students = 54 #if this is done and when you will call objectname.number_of_students this value will be called
                                       #And if not objectname.number_of_students will take the value from static variable of class if exists
    def fetchlastdata(self):
        if(_6e.number_of_students == self.number_of_students): #this check shows what is the difference between instance namespace and class namespace
            print("The total Number of Student::",self.number_of_students)
        else:
            print("Total Number was changed to::",self.number_of_students)    
        print("The Name of Student is::",self.name)
        print("Roll Number of student is::",self.roll_no)
        print("Univeristy Identity number::",self.uni_id)
        print("Contact detail::",self.contact_no)


exit = 0
while exit!=1:
    exit = int(input("Enter 1::to Terminate now ,2::to register a student under Class 6 Section E ,3::to fetch the last student data,4::to Print the format::"))
    if exit == 2:
        stud = _6e()
        name = input("Enter The Name of Student::")
        roll_no = input("Enter Roll number of student::")
        uni_id = input("Enter Id Provided by University to the student upon admission::")
        contact_no = input("Enter Contact Number of Student::")
        stud.registerStudent(name,roll_no,uni_id,contact_no)
    elif exit == 4:
        print("Printing The Format Only")
        print("Total Number of student in Class 6 E::",_6e.number_of_students)
        print("Enter The Name of Student::",_6e.name)
        print("Enter Roll number of student::",_6e.roll_no)
        print("Enter Id Provided by University to the student upon admission::",_6e.uni_id)
        print("Enter Contact Number of Student::",_6e.contact_no)
    elif exit == 3:
        try:
            stud.fetchlastdata()
        except:
            print("NO registration done yet")
        finally:
            pass     
    else:
        pass

   