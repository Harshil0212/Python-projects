from colorama import Fore
import colorama
import random
colorama.init()
d1={}
n=int(input("enter limit="))
for i in range(1,n+1):
    employenumber=i
    salary=random.randint(10000,20000)
    d1[employenumber]=salary
print(d1)
record=int(input("entre number="))
c=0
for k,v in d1.items():
    if k==record:
        print("employenumber\tsalary")
        print(k,"\t",v,record)
        c=1
        break

if c==0:
    print("Not found")