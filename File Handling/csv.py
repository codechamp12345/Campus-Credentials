import csv 
f = open("student.csv","a",newline="")
a = csv.writer(f)#
# a.writerow(["StudentID","Roll No","Name","Mobile No"])
f.close()

import csv 
f = open("student.csv","a",newline="")
a = csv.writer(f)

StudentID = int(input("Enter Student ID: "))
RollNo = int(input("Enter Roll No: "))
name = input("Enter Name: ")
mobileNo = int(input("Enter Mobile No: "))

a.writerow([StudentID,RollNo,name,mobileNo])
print("Student record has save")
f.close()
