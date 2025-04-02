container = [2,1,4,5,5,4,4,1,1]
count = 0;
even = 0; #even=1
odd = 0;
for i in container:
    if i == 4:
        count+=1
    elif i ==2:
        even+=1
    elif i==5:
        odd+=1
print(count-even)
print(count-odd)