n = int(input("n = "))
for i in range(4, n + 1, 4):
    print(i, end=" ")

# OR

n = int(input("n = "))
for i in range(4, n + 1):
    if i % 4 == 0:
        print(i, end=" ")
