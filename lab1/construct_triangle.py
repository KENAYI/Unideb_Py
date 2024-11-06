import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("The triangle can be constructed!")
    p = (a + b + c) / 2
    A = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("A = {0:.2f}".format(A))
else:
    print("The triangle cannot be constructed!")
