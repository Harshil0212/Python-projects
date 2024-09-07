import calendar
year=int(input("enter year="))
for i in range(1,13):

    cal=calendar.month(year,i)
    print(cal)