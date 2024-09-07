from colorama import Fore
p=0
f=0
import colorama
import random
colorama.init()
d1={}
n=int(input("Enter limit =>"))
for i in range(1,n+1):
    no=i
    marks=random.randint(1,30)
    d1[no]=marks
print("No\tmarks")
print("-*-"*20)
for k,v in d1.items():
        if v>15:
            p=p+1
            print(Fore.BLUE,k, "\t", v,"\tpass",)
        else:
            f=f+1
            print(Fore.RED,k,"\t",v,"\tfail",)
print("Pass student = ",p," Fail student = ",f)



