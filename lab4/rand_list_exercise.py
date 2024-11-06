import random

# Task: Generate a random list of numbers and analyze it
# Step 1: Input the number of elements in the list
n = int(input('n='))

# Step 2: Create a list of random numbers between 1 and 10
list = [random.randint(1, 10) for i in range(n)]

# Step 3: Filter out the even numbers from the list
even = [i for i in list if i % 2 == 0]

# Step 4: Filter out the odd numbers from the list
odd = [i for i in list if i % 2 != 0]

# Step 5: Check if the list contains only even numbers
evens = False
if even == list:
    evens = True

# Step 6: Print the generated list
print(list)

# Step 7: Print the sum of all elements in the list
print("Sum =", sum(list))

# Step 8: Print whether all elements are even
print("Evens =", evens)

# Step 9: Print the minimum value in the list
print("Min =", min(list))

# Step 10: Print the maximum value in the list
print("Max =", max(list))

# Step 11: Print the even elements sorted in ascending order
print("Even elements =", sorted(even))

# Step 12: Print the odd elements sorted in descending order
print("Odd elements =", sorted(odd, reverse=True))
