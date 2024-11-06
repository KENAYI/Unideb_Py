# Importing the sys module to read from standard input (stdin)
import sys

# Looping through each line from the standard input (stdin)
for line in sys.stdin:
    # Print the current line
    print(line)

# Infinite loop to continuously accept user input
while True:
    try:
        # Take an input from the user
        line = input()
        # Print the inputted line
        print(line)
    except EOFError:
        # If an EOF (End-of-File) error occurs, break out of the loop
        break
