# list
# tuple
# dictionary

# mylist = ["Prashant","Ashish","Komal","Ankush","Ashish",77,"Sandip",70.23,"Prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# list is a mutable means we can change the data

# mylist[0]="Akshay"
# print(mylist)

# if "Ankush" in mylist:
#     print("yes ankush is available")
# else:
#     print("Not available")

#add item at the end of list

# mylist.append("Chaitanya")
# print(mylist)

#to add item at specific position in list
# mylist.insert(1,"sanket")
# print(mylist)

# mylist.remove("Sandip")
# print(mylist)

# Clone the list into another variable
# newlist = mylist.copy()
# print(newlist)

# mylist= [['Prashant','Jha'],[85.56],[44022,"yyy"]]

# print("Multidimensional List")
# print(mylist)
# print(mylist[0][0])      #Prashant
# print(mylist[0][1])      #Jha
# print(mylist[1][0])      #85.56
# print(mylist[2][0])      #44022
# print(mylist[2][1])      #yyy

# list1 = ["Chaitanya","Khurd"]
# print(list1*2)

# add two list
# list2 = [40,20.90]
# print(list1+list2)

# list2 = [40,20.90,"Chaitanya"]
# del list2[2]
# print(list2)

# # delete entire list
# del list2
# print(list2)


# it will writtens empty list
# list2 = [40,20.90,"Chaitanya"]
# list2.clear()
# print(list2)

# name = "Chaitanya"  #string
# print(name)
# print(type(name))
# # using list constructor
# myname = list(name)
# print(myname)

# mylist = [10,20,30,40]
# mylist.reverse()
# print(mylist)

# Sorts list in ascending order
mylist = [44,22,77,0,9,88]
mylist.sort()
print(mylist)