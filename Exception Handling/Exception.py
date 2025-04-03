# a = int(input("Enter First No:"))
# b = int(input("Enter Second No:"))
# try:
#     print(a+b)
# except:
#     print("Enter valid input")

# try:
#     a=int(input("Enter First integer No:"))
#     b=int(input("Enter Second integer No:"))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("Please ensure that you can't divide by zero")
# except ValueError as message:
#     print("Enter only integer no=>",message)

# try:
#     a=int(input("Enter First integer No:"))
#     b=int(input("Enter Second integer No:"))
#     print(a/b)
# except (ValueError,ZeroDivisionError) as message:
#     print(message)      

try:
    a=int(input("Enter First integer No:"))
    b=int(input("Enter Second integer No:"))
    print(a/b)
# except:
#     print("This is default exception") #write default exception block in the end of all block
except (ValueError,ZeroDivisionError) as message:
    print(message)      
except:
    print("This is default exception") #default block  

