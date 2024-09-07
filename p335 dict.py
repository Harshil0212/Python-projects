import random
d1={}
n=int(input("enter limit="))
for i in range(1,n+1):
    enrollment=i
    name=random.randint(1,50)
    d1[enrollment]=name
print(d1)
record=int(input("enter number="))
for k,v in d1.items():
    if k==record:
        print("enrollment\tname")
        print(k,"\t",v)


