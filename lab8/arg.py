import sys

argc = len(sys.argv)
print('Number of arguments: ', argc)

print('File location: ', sys.argv[0])

print('Arguments: ')

p = 1
for i in range(2, argc):
    p = p * int(sys.argv[i])
print("Product: ", p)