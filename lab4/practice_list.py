# Task 1: Capitalize the first letter of each word in a list
# Input: ['anthony', 'blake', 'charlotte']
# Output: ['Anthony', 'Blake', 'Charlotte']

# Solution 1
l = ['anthony', 'blake', 'charlotte'] 
new = [x[0].upper() + x[1:] for x in l]
print(new)

# Solution 2
l = ['anthony', 'blake', 'charlotte']
new = [x.capitalize() for x in l]
print(new)


# Task 2: Initialize a 10-item list with all 0's
# Input: []
# Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

new = [0 for i in range(10)]
print(new)


# Task 3: Multiply each number in the list by 2
# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = [2 * i for i in l]
print(new)


# Task 4: Convert a list of strings into a list of integers
# Input: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
new = [int(i) for i in l]
print(new)


# Task 5: Convert a string of digits to a list of integers
# Input: "1234567"
# Output: [1, 2, 3, 4, 5, 6, 7]

s = "1234567"
new = [int(c) for c in s]
print(new)


# Task 6: Find the length of each word in a sentence
# Input: 'The quick brown fox jumps over the lazy dog'
# Output: [3, 5, 5, 3, 5, 4, 3, 4, 3]

s = 'The quick brown fox jumps over the lazy dog'
new = [len(c) for c in s.split()]
print(new)


# Task 7: Collect the first letter of each word in a string
# Input: "python is an awesome language"
# Output: ['p', 'i', 'a', 'a', 'l']

s = 'python is an awesome language'
new = [c[0] for c in s.split()]
print(new)