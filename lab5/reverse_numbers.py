# Continuously take user input, split into words, and reverse the order of words
# until '0' is entered as the first word in the line


while True:
    # Read the input line and split it into a list of integers
    line = input().strip()
    numbers = list(map(int, line.split()))
    
    # If the first number is 0, break the loop and stop processing
    if numbers[0] == 0:
        break
    
    # Remove the first number (count) and reverse the remaining list
    reversed_numbers = numbers[1:][::-1]
    
    # Print the reversed list with each number separated by a space
    print(" ".join(map(str, reversed_numbers)))

# OR

# # Read the first line of input and split it into a list of words
# line = input("Enter a line of text (start with '0' to stop): ").split()

# # Loop until the first word in 'line' is '0'
# while line[0] != '0':
#     # Reverse the list of words, excluding the first word
#     rev = line[:0:-1]

#     # Join the reversed list into a single string with spaces
#     revstr = ' '.join(rev)

#     # Print the reversed string
#     print(revstr)

#     # Read the next line of input and split it into a list of words
#     line = input("Enter a line of text (start with '0' to stop): ").split()


# OR

# # Read the first line of input and split it into a list of words
# line = input("Enter a line of numbers (start with '0' to stop): ").split()

# # Loop until the first element in 'line' is '0'
# while line[0] != '0':
#     # Reverse the list of elements, excluding the first one
#     reversenum = list(reversed(line[1:]))

#     # Print the reversed list, unpacked into separate elements
#     print(*reversenum)  # The * operator unpacks the list for space-separated output

#     # Read the next line of input and split it into a list of words
#     line = input("Enter a line of numbers (start with '0' to stop): ").split()
