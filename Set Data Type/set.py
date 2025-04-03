# in the set data type you cannot access the data using indexing because its have random indexing
#mutable

# myset = {1,2,"sanjay",5.66,"rahul","ayush","ramesh","ankit"}
# print(myset)
# print(type(myset))

# myset.add(60)
# print(myset)

#no error
# myset.discard(3) #3 is not present in the set
# print(myset)

# error 
# myset.remove(3) #3 is not present in the set
# print(myset)

#union operation combines both sets and gives the random combination of both data type
# myset = {10,20,30,40}
# yourset = {"Chaitanya","Khurd"}
# newset = myset.union(yourset)
# print(newset)

# intersection ==> Returns the common elements between two sets
# myset = {10,20,30,40}
# yourset = {"Chaitanya","Khurd",10}
# newset = myset.intersection(yourset)
# print(newset)

# differnce ==> it will returns the element which is present in the first set but not in second set
# myset = {10,20,30,40}
# yourset = {10,50,60,30}
# print(myset.difference(yourset))

#clear fn used to clear the data

# myset  = {10,20,30,40}
# print(myset.pop())
# print(myset.clear())