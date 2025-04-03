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

