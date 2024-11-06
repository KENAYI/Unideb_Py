n = int(input("n = "))
counter = 0

while n != 0:
    counter = counter + 1
    n = n // 10

print("Digits =", counter)
