n = int(input("n = "))
f = 1

for i in range(1, n + 1):
    f *= i

print("{0}! = {1}".format(n, f))

# OR

n = int(input("n = "))
f = 1

for i in range(n, 0, -1):
    f *= i

print("{0}! = {1}".format(n, f))
