list1 = [5,3,9,2,8]
max = min= list1[0] # max=5 and min=5

for i in range(len(list1)): #i=0
    if list1[i] > max:
        max=list1[i]

    if list1[i] < min:
        min = list[i]

print(max)
print(min)