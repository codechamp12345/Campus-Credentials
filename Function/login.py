def login():
    username = input("Enter Your Username:")
    password = input("Enter Your Password:")
    if username == password:
        print('login successfully!')
    else:
        print("You have enetered wrong credentials")

login()


def info(fname,lname):#parameter
    print("Firstname:",fname)
    print("Lastname:",lname)

info("Chaitanya","Khurd") #calling fn


def arithmetic(a,b):
    r = a + b
    n = a - b
    m = a * b
    return r,n,m #fixed so it will returns result in the form of tuple

result = arithmetic(10,6)  #calling fn
print("Result:",result)


def func(fname,lname):#called fn
    print("Hi",fname)
    print("Hi",lname)
func(fname="Chcaitanya",lname="Khurd")#calling fn

# User input
fname = input("Enter First Name:")
lname = input("Enter last Name:")
func(fname,lname)

# variable length arg
# variable number of args

def nameOfCity(*city):
    print("Name of city=",city)

nameOfCity("Mumbai","Pune","Nagpur","Nashik")



