year = int(input("Year = "))
month = int(input("Month = "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    day = 31
elif month == 4 or month == 6 or month == 9 or month == 11:
    day = 30
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        day = 29
    else:
        day = 28
else:
    print("Wrong value!")
    day = 0

print("Number of days =", day)
