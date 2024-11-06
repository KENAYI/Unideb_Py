a = int(input("a = "))
b = int(input("b = "))
s = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        s += i

print("Sum =", s)
