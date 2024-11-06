# Initialize variables for the sum and count of numbers
sum = 0
c = 0

# Infinite loop to keep asking for input
while True:
    try:
        # Take an integer input and add it to the sum
        sum += int(input())
        
        # Increment the count of numbers
        c += 1
    
    # Catch the EOFError if the user presses CTRL+D (End-of-File signal)
    except EOFError:  # EOF – CTRL+D
        break

# After the loop ends (when CTRL+D is pressed), calculate and print the average
print("{0:.2f}".format(sum / c))
