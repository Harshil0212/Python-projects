import random
list1=[]
list2=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(65,90)
    ch=chr(y).lower()
    list1.append(ch)
for ch in list1:
    if ch=="i" or ch=="a" or ch=="e" or ch=="o" or ch=="u":
        list2.append("7")
    else:
        list2.append(ch)

print(list1)
print(list2)

