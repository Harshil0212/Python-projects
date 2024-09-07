month=int(input("entre number of month="))
year=int(input("entre number of year="))

if month==1 or month==3:
    print("Days 31 in ",year)
elif month==4 or month==6:
    print("Days 30 in ",year)
elif month==5 or month==7:
    print("days 31 in",year)
elif month==8 or month==10:
    print("day 31 in month",year)
elif month==9 or month==11:
    print("day 30 in month",year)
elif month==12:
    print("days 31 in month",year)

else:
    if year%4==0:
        print("Leap year 28 days in ",year)
    else:
        print("30 days in",year)
