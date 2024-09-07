import random
list1=[]
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    y=random.randint(65,90)
    ch=chr(y).lower()
    list1.append(ch)

print(list1)

c1=0
c2=0
for ch in list1:
    if ch=="i" or ch=="a" or ch=="e" or ch=="o" or ch=="u":
        print(ch,"is wovel")
        c1+=1
    else:
        print(ch,"it's not wovel")
        c2+=1
print("Vowels are ",c1," Other are ",c2)