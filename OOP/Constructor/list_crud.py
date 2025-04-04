import sys

class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentID=[]
        self.studentName=[]
        self.studentRollNo =[]
        self.studentCity=[]

    def addStudent(self):
        self.studentID.append(int(input("Enter Student ID:")))
        self.studentName.append(input("Enter Student Name:"))
        self.studentRollNo.append(int(input("Enter Student Roll No:")))
        self.studentCity.append(input("Enter Student City:"))
        print("Student Record Added Successfully")

    def displayStudent(self):
        for i in range(len(self.studentID)):
            print(self.studentID[i],self.studentName[i],self.studentRollNo[i],self.studentCity[i])

    def searchStudent(self):
        searchID=int(input("Enter Student ID to Search:"))
        for i in range(len(self.studentID)):
            if self.studentID[i]==searchID:
                print(self.studentID[i],self.studentName[i],self.studentRollNo[i],self.studentCity[i])
                return # Exit the function if student is found
        print("Student Record Not Found")
            
    def deleteStudent(self):
        deleteID=int(input("Enter Student ID to Delete:"))
        for i in range(len(self.studentID)):
            if self.studentID[i]==deleteID:
                self.studentID.pop(i)
                self.studentName.pop(i)
                self.studentRollNo.pop(i)
                self.studentCity.pop(i)
                print("Student Record Deleted Successfully")
                return # Exit the function if student is found
        print("Student Record Not Found")

    def updateStudent(self):
        updateID=int(input("Enter Student ID to Update:"))
        for i in range(len(self.studentID)):
            if self.studentID[i]==updateID:
                self.studentName[i]=input("Enter Student Name:")
                self.studentRollNo[i]=int(input("Enter Student Roll No:"))
                self.studentCity[i]=input("Enter Student City:")
                print("Student Record Updated Successfully")
                return # Exit the function if student is found
        print("Student Record Not Found")
        
obj = CRUD() # Create the object outside the class
while True:
    print("\n1.Add Student\r\n2.Display Student\r\n3.Search Student\r\n4.Delete Student\r\n5.Update Student\r\n6.Exit")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        obj.addStudent()  #function
    elif choice == 2:
        obj.displayStudent()  #function
    elif choice == 3:
        obj.searchStudent()  #function
    elif choice == 4:
        obj.deleteStudent() #function
    elif choice == 5:
        obj.updateStudent()  #function
    elif choice == 6:
        break # Use break to exit the loop
    else:
        print("Invalid Choice")