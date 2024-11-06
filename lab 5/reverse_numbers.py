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
