import colorama
from colorama import Fore, Back, Style
colorama.init()
marks=int(input("ENTER THE MARKS=>"))

if marks>20:
    print(Fore.GREEN," VERY GOOD")
else:
    print(Fore.BLUE," DO HARD WORK")