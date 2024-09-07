from colorama import Fore
import random
import colorama
colorama.init()
good=1

d1 = {}

n = int(input("Enter limit =>"))
s= int(input("enter salary="))
for i in range(1, n + 1):
    employenumber = i
    salary = random.randint(10000, 20000)
    d1[employenumber] = salary
print("employee number\tsalary")
print("-*-" * 20)
for k, v in d1.items():
    if v > s:
        good=good+1
        print(Fore.GREEN,k, "\t", v, "\tGood salary")



print("good salary=",good,)

