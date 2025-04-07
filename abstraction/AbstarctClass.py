# An abstract class can be considered as a blueprint for other classes It allows you to craete a set of methods that must be created within any child classes built from  the abstract class 


from abc import ABC
class Help4code(ABC): #Abstarct Class
    @abstractmethod #decorator
    def training(self): #abstract method
        pass
    @abstractmethod  #Abstract method
    def placement(self):
        pass

class Ashish(Help4code):
    def training(self):
        print('c c++ java')
    def placement(self):
        print("Java Placement")

class Chaitanya(Help4code):
    def training(self):
        print('Python | Django')
    def placement(self):
        print("Data Science Placement")

obj1 =Ashish()
obj1.training()
obj1.placement()

obj2 = Ankush3)
obj2.training()
obj2.placement()

obj3 = Chaitanya()
obj3.training()
obj3.placement()


