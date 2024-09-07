import random
list1=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(65,90)
    ch=chr(y)
    list1.append(ch)

print(list1)