import emoji
import colorama
from colorama import Fore
colorama.init()
n=int(input("enter marks="))
if n>15:
    print(Fore.GREEN,"very good",emoji.emojize(":thumbs_up:"))
else:
    print(Fore.RED,"not good",emoji.emojize(":thumbs_down:"))
