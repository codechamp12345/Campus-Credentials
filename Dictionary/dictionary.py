# In dictionary we represent data in as key value pair
# Dictionary represented by {key:value} parenthesis
# Duplicate keys are not allwed
# Duplicate values are allowed
# By the nature dictionary is growable
# it is mutable
# unoredered data


mydict = {
    101: 'rashant',
    102: 'ashish',
    '103':'mohini',
    '104':'trivani', #different data type
    101: 'ashish',  #update 101
    104: 'ashish'
    }
print(mydict)

# with the help of key we have to print values
# a = mydict[102]
# print(a)

# replace old value by new value
# mydict[102]="peter"
# print(mydict)

# only print key
# for x in mydict:
#     print(x)

# print values
# for x in mydict.values():
#     print(x)

# printing both keys and values
# for x,y in mydict.items():
#     print(x,y)

# add a new key and value 
# mydict["mobile no"] = 9898079787
# print(mydict)

# mydict = {
#     101:"Chaitanya",
#     "Preofession":"Developer",
#     "id":1001
# }
# print(mydict)
# pop
# mydict1.pop(101)
# print(mydict1)

# newdict = mydict.copy()
# print(newdict)

