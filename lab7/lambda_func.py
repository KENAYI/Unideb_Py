# Lambda with arithmetic operations
print((lambda x, y, z: (x + y + z) * 10)(1, 2, 3))

# Lambda with sorting
list = ["Jabba", "Han", "Luke"]
print(sorted(list, key = lambda item: -len(item)))
