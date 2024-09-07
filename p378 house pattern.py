import colorama
from colorama import Fore,Back,Style
colorama.init()
n=int(input("enter limit="))
print(Fore.GREEN,"-*-"*10)
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(Fore.BLUE,"*",end="")
    print("")
for i in range(1,n+1):
    for j in range(1, i + 1):
        print(Fore.BLUE, "*", end="")
    for j in range(n,i-1,-1):
        print(Fore.BLUE, "*", end="")
    print("")
