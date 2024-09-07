list1=[20,50,45,65,20]
list2=[20,11,15,12,33]
list3=[22,14,15,16,17]

for i in list1:
    if i%2==0:
        list2.append(i)
    else:
        list3.append(i)

print(list1)
print(list2)
print(list3)