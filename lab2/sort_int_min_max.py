n = int(input("n = "))
min_value = n
max_value = n

while n != 0:
    if n < min_value:
        min_value = n
    if n > max_value:
        max_value = n
    n = int(input("n = "))

print("Min =", min_value)
print("Max =", max_value)
