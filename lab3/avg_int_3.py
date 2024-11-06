# Initialize variables to store the sum of numbers and count of numbers
sum = 0
c = 0

# Take the first number as input
n = int(input())

# Continue until the input number is 0
while n != 0:
    # Add the input number to the sum
    sum += n
    
    # Increment the count of numbers
    c += 1
    
    # Take the next number as input
    n = int(input())

# Calculate the average by dividing the sum by the count and print it with 2 decimal places
print("{0:.2f}".format(sum / c))
