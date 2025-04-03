
#Binary files
# rb==>read binary 
# wb==>write binary
f1 = open("scr1.jpg","rb") # reading the image file
f2 = open("scr2.jpg","wb") # writing the image file
data = f1.read()
f2.write(data)                  
print("Image copied successfully")



