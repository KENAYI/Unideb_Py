n = int(input("n = "))
i = 2

while n > 1:
    if n % i == 0:
        n /= i
        if n != 1:
            print(i, end=" ")
        else:
            print(i)
    else:
        i += 1
