import random
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
            print(k, "\t", v,"\tpass")
        else:
            print(k,"\t",v,"\tfail")


