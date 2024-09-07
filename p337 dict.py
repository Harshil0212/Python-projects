b0=0
import random
d1={}
n=int(input("enter limit="))
for i in range(1,n+1):
    number=i
    m1=random.randint(1,40)
    m2=random.randint(1,30)
    m3=random.randint(1,50)
    d1[number]=[m1,m2,m3]
print(d1)
for k,v in d1.items():
    m1,m2,m3=v
    t=sum(v)
    print(k,"\t",m1,m2,m3)
    b0=1+t
print("total=",b0)