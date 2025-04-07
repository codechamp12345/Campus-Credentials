# Stack Implementation without size
# 1) Push()
# 2) Pop()
# 3) Peek()
# 4) IsEmpty()
# 5) Isfull()
# 6) Delete()
# 7) Display()

class Stack:
    def __init__(self):   #constructor
        self.myStack = [] #python represent the stack using lint DS

    #push method
    def push(self,data):
        self.myStack.append()
        print("Push Element is done!!!")

    #Display stack
    def display(self):
        print(self.myStack)

    #Pop Operation
    def POP(self):
        print("The Element POP:",self.myStack.pop())

    #Peek Operation
    def Peek(self):
        print("Top Element:",self.myStack[-1])


    #Stack is empty
    def isEmpty(self):  
        if self.myStack ==[]:
            return True
        else:
            return False


obj= Stack() #object os stack
print("Stack has Created!!!")

if __name__ =='__main__':
    while True:
        print('1.Push Operation')
        print('2.Pop Operation')
        print('3.Peek Operation')
        print('4.isEmpty Operation')
        print('5.Display Operation')
        print('6.Delete Operation')
        print('7.Exit')
        print()
        ch = input("Enter Your Choice:")
        if ch ==1:
            data = int(input('Enter the element for stack:'))
            obj.push(data)
        elif ch == 2:
            obj.POP()
        elif ch == 3:
            obj.Peek()
        elif ch ==4:
            print(obj.isEmpty())
        elif ch == 5:
            obj.displayStack()
        elif ch ==7:
            sys.exit()
        




