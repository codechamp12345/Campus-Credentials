'''
Encapsulation is a process of protecting the data and functionality in a single unit
This mechanism is often used to protect the data of an object from other objects .Its one of the fundamental principal in any programming language that supports OOP
We can protect the varibles in the class by making them as a private 
we need to add two under score as a prefix to make variable private 
once we can make a variable as a private .we can acesss them privately
'''

# class Base: #parent class
#     print("Parent class constructor called")

#     self.a  = "Chaitanya" #public data member
#     self.__c  = "Ashish" #private member

# #creating a derived class child class
# class Derived(Base):  #child class
#     def __init__(self):
#         #calling constructor of base class
#         Base.__init__(self)
#         print("Calling privae member of a base class")
        #print(self.a)
        #print(self.__c)

# obj1 =  Derived()
# print(obj1.a)
# print(obj1.__c)

#obj2 = Base()
#print(obj2.__c)

class Rbi:
    #declaring public methid
    def publicPolicy(self):
        print("Check the public policy")

    #declaring private method
    def __privatePolicy(self):
        print("There is some private policy which is not accessible for public")

Class Sbi(Rbi):
    def __init__(self):
        Rbi.__init__(self) #second parent class

    def callingPublicMethod(self):   #chid class public method
        print("\n Insid chid class")
        self.publicPolicy()

    def callingPrivateMethod(self):
        self.__privatePolicy()

obj1 = Sbi()
obj1.callingPublicMethod()
obj1.callingPrivateMethod()

obj1.publicPolicy()
obj1.__privatePolicy()

obj2 = Rbi()
obj2.__privatePolicy()
obj2.publicPolicy()

        


