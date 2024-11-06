n = int(input("n = "))
sum = 0

while n != 0:
    sum += n % 10
    n = n // 10

print("Sum of digits =", sum)
