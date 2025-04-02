list1 = [0,1,0,3,12]
for i in list1:
    if i==0:
        list1.remove(i)
        list1.append(i)
print(list1)