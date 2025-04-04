class College:
    collegename = "Modern College" #static variable
    def __init__(self):
        self.studentname = "Chaitanya"  #instance variable(3 seprate memory)

principal = College() #Object creation
teacher = College()
accountant = College()

print("principal=",principal.collegename,".....",principal.studentname)
print("teacher=",teacher.collegename,".....",teacher.studentname)
print("accountant=",accountant.collegename,".....",accountant.studentname)
College.collegename = "HBD" #second way to add ststic vcariable

principal.studentname = "Chaitanya khurd"
print("principal=",principal.collegename,"|",principal.studentname)
print("teacher=",teacher.collegename,"|",teacher.studentname)
print("accountant=",accountant.collegename,"|",accountant.studentname) 

