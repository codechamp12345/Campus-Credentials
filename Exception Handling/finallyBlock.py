# try:
#     a=int(input("Enter First integer No:"))
#     b=int(input("Enter Second integer No:"))
#     print(a/b)
# # except:
# #     print("This is default exception") #write default exception block in the end of all block
# except (ValueError,ZeroDivisionError) as message:
#     print("Enter correct number:",message)      
# finally:
#     print("I will always executed") 

try:
    a=int(input("Enter First integer No:"))
    b=int(input("Enter Second integer No:"))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)      
except ValueError as msg:
    print(msg)

