#Where we can decalre static variable?
# inside a class but outside of method
#in a constructor by using class name
#in a instance method by using class name
#in a static method by using class name

#where we can access static variable?
#inside a class by using self variable or class name
#inside a constructor by using self variable or class name
#inside a instance method by using self variable or class name
#inside a static method by using class name
#outside a class by using class name

#how do we delete the static variable?
#using del keyword
# del classname.staticvariable
# inside classmethod we can use cls variable : del cls.staticvariable

class Hod:
    def __init__(self):
        self.name = "Chaitanya"  #instance variable(3 seprate memory)
        print("myname =",self.name)

obj = Hod()
obj.self()

