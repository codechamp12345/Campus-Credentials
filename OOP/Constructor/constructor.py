# class NewClass:
#     def __init__(self): #constructor declaration
#         print("my name is constructor i always execute first")
#     def show(self):
#         print("Welcome to class level programming")\

# obj = NewClass()#creating a object
# print(obj)
# obj.show()
# obj1 = NewClass()


class Hod:
    def __init__(self):  #constructor declaration
        self.name = "Chaitanya"
        self.age = 21
        self.empid = 1001

    def info(self): #instance method
        print("my name is:",self.name)
        print("my age is:",self.age)
        print("my empid is:",self.empid)

obj = Hod() #object creation
obj.info()