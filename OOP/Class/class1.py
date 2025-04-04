class Student:
    rollno = 101
    num1 = 50
    num2 = 100 #data transfer

    def add(self):  #member function
        print(self.num1 + self.num2)   #150
        self.name =input("Enter name:") #name is your new type of variable
        print(self.name)

obj = Student()  #creating a object of class and we always create a object outside a class

obj.add()  #calling function
print(obj.rollno)   
