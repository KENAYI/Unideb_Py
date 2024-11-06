import math

print("Input the coefficients of the second-degree equation!")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == 0:
    if b == 0:
        print("Error!")
    else:
        x = -c / b
        print("First-degree, x =", x)
else:
    d = b * b - 4 * a * c
    print("The value of the discriminant:", d)

if d > 0:
    print("Two real solutions.")
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print("x1 =", x1)
    print("x2 =", x2)
elif d == 0:
    x = -b / (2 * a)
    print("One solution:", x)
else:
    print("No real solution!")
