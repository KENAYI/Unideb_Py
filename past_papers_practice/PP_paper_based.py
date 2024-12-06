#5
# # Start a for loop from 18 down to 6, decrementing by 2
# for i in range(18, 5, -2):  
#     # For each value of i, divide it by 2 and subtract 2, then print the result
#     print(i / 2 - 2)  


# 6
# # Initialize variable a to 0
# a = 0  

# # Loop through numbers from 1 to 5 (inclusive)
# for i in range(1, 6):  
#     # Check if i is even
#     if i % 2 == 0:  
#         # If i is even, add i to a
#         a += i  
#     else:
#         # If i is odd, subtract i from a
#         a -= i  

# # Print the final value of a after the loop
# print(a)


# 7
# # Initialize x to 12
# x = 12  

# # Start a while loop that runs as long as x is greater than 0
# while x > 0:
#     # Check if x is divisible by 4 
#     if x % 4 == 0:
#         print(x)  # If x is divisible by 4, print the current value of x
#     x -= 2  # Decrease x by 2 for each iteration


# # Iterate over values from 12 down to 2, decrementing by 2
# for x in range(12, 0, -2):
#     # Check if x is divisible by 4
#     if x % 4 == 0:
#         print(x)

# 8
# # Create a list of numbers from 1 to 20 (inclusive)
# numbers = [i for i in range(1, 21)]

# # Create a new list by adding 2 to each number that is divisible by 3
# res = [i + 2 for i in numbers if i % 3 == 0]

# # Print the resulting list
# print(res)
