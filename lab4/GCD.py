# Take input from the user in a single line
line = input()

# Split the input string into a list of words (separated by spaces)
s = line.split(" ")

# Convert the first and second elements of the list to integers
a = int(s[0])
b = int(s[1])

# Initialize the greatest common divisor (gcd) as 1
gcd = 1

# Determine the smaller of the two numbers to limit the loop
if a < b:
    c = a
else:
    c = b

# Loop from 2 to the smaller number (c) to find the greatest common divisor
for i in range(2, c + 1):
    # If both numbers are divisible by 'i', set 'gcd' to 'i'
    if (a % i == 0 and b % i == 0):
        gcd = i

# Print the greatest common divisor
print(gcd)
