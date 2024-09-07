import random
d1={}

n=int(input("Enter limit =>"))
for i in range(1,n+1):
    employenumber=i
    salary=random.randint(10000,20000)
    d1[employenumber]=salary
print("employee number\tsalary")
print("-*-"*20)
for k,v in d1.items():
        if v>15000:

            print(k,"\t",v,"\tGood salary")
        else:
            print(k,"\t",v,"\tDo ur best")

print(d1)