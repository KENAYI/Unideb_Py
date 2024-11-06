# Take input from the user as a single line
line = input()

# Split the input string into a list of strings (separated by space)
s = line.split(" ")

# Convert the first and second elements of the list to integers
a = int(s[0])
b = int(s[1])

# Continue reducing a and b until they are equal
while a != b:
    # If a is greater than b, subtract b from a
    if a > b:
        a = a - b
    # If b is greater than a, subtract a from b
    else:
        b = b - a

# After the loop, check if the common value is 1
if a == 1:
    print("YES")  # If the numbers are coprime (GCD = 1), print "YES"
else:
    print("NO")  # If the GCD is not 1, print "NO"
