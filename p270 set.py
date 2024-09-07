import random
set1=set()

n=int(input("enter limit ->"))
for i in range(1,n+1):
    y=random.randint(1,20)
    set1.add(y)

print(set1)