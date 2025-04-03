import csv 
import csv 
f = open("studentRecords1.csv","a",newline="")
a = csv.writer(f)
# a.writerow(["rollno","name","mobileno","EmailId","p1","p2","p3","total","percentage","result"])
f.close()

rollno = int(input("Enter Student rollno: "))
name = input("Enter Name: ")
mobileno = int(input("Enter Mobile No: "))
EmailId = input("Enter EmailId: ")
p1 = int(input("Enter Marks in P1: "))
p2 = int(input("Enter Marks in P2: "))
p3 = int(input("Enter Marks in P3: "))

total = p1+p2+p3
percentage = total/3
if percentage >= 40:
  result = "Pass"
else:
  result = "Fail"

f = open("studentRecords1.csv","a",newline="") #reopen the file in append mode
a = csv.writer(f)
a.writerow([rollno,name,mobileno,EmailId,p1,p2,p3,total,percentage,result])
f.close()


#program to read data from csv file
# f = open("studentRecords1.csv","r")
# a = csv.reader(f)
# for i in a:
#   print(i)
# f.close()




f = open("studentRecords1.csv", "r")
a = csv.reader(f)

next(a, None)  

for row in a:
    print(", ".join(row)) 

f.close()









