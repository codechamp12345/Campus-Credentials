f = open("file.txt","w")
print("name of file:",f.name)
print("mode of file:",f.mode)
print("readable:",f.readable())
print("writable:",f.writable())
print("is file closed:",f.closed)
f.close()
print("is file closed:",f.closed)

# performing write operations
f = open("file.txt","a")
f.write("\n Nagpur is a smart city")
f.close()
print("File Operation is done")


# performing read operations
f = open("file.txt","r")
print(f.read())
f.close()

# inserting list
f = open("file.txt","a")
mylist = ["Chaitanya","Prahshant","Mahesh"]
f.writelines(mylist)
f.close()
print("File Operation is done")


#tuple

f = open("file.txt","a")
mylist = ("CM","Hii","Hello")
f.writelines(mylist)
f.close()
print("File Operation is done")

#dictionary

f = open("file.txt","a")
mylist = {"CM":"Hii","Hii":"Hello"}
f.writelines(mylist)
f.close()
print("File Operation is done")


with open("file.txt","w") as f:
    f.write("Hello World1\n") 
    f.write("Hello World2\n") 
    f.write("Hello World3\n") 
    print("File closed:",f.closed) 

with open("file.txt","r") as f:
    content = f.read()
    print(content)

