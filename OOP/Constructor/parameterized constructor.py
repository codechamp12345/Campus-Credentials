# class Hod:
#     def __init__(self,name,age,rollno): #parameterized constructor 
#         self.name = name
#         self.age = age
#         self.rollno = rollno
    
#     def show(self):
#         print('name=',self.name)
#         print('age=',self.age)
#         print('rollno=',self.rollno)

# obj = Hod("Chaitanya",21,1001)
# obj.show()


# class New:
#     def __init__(self):
#         self.a = 10
# Obj1 = New()
# Obj2 = New()
# Obj3 = New()
# Obj1.a = 20
# print(Obj1.a)
# print(Obj2.a)
# print(Obj3.a)




# class Student():
#     def __init__(self):
#         self.s_name = "Chaitanya"
#         self.s_age = 21
#         self.s_rollno = 1001


#declaring instance variable inside a instancxe method by using self variable

class Student:
    def __init__(self): #constu=ructor
        self.s_name = "Chaitanya"
        self.s_rollno = 1001
        self.branch = "CSE"

    def getdata(self): #instance method
        self.s_mb = 9898079787 #instance variable

obj = Student() #until and unless we call the method it will not execute
#obj.getdata()
print(obj.__dict__)
print(obj.s_mb)

