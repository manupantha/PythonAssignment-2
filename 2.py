year = int(input("enter the year you want to check: "))
if year % 4 == 0 and year % 100 != 0:
    print("the year is leap year ")
elif year % 400 == 0:
    print("the year is leap year")
elif year % 100 != 0:
    print("the year is not leap year")
else:
    print("the year is not leap year")
