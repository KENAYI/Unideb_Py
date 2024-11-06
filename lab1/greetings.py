hour = int(input("hour = "))

if hour > 5 and hour < 12:
    print("Good Morning!")
elif hour >= 12 and hour < 18:
    print("Good Afternoon!")
elif hour >= 18 and hour < 22:
    print("Good Evening!")
elif (hour >= 22 and hour < 24) or (hour >= 0 and hour <= 5):
    print("Good Night!")
else:
    print("Wrong value!")
