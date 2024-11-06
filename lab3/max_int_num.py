# Get the number of inputs from the user
n = int(input())

# Variable to track if it's the first number
first = True

# Loop through all the inputs
for i in range(n):
    # Take a number as input from the user
    num = int(input())
    
    # If it's the first number, set it as the initial max value
    if first:
        max_num = num
        first = False  # Mark that the first number has been processed
    
    # If the current number is greater than the current max_num, update max_num
    if num > max_num:
        max_num = num

# After the loop finishes, print the maximum number
print(max_num)
