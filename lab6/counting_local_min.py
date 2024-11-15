# Count local minimums from given lists

import sys

def count_of_local_minimums(lst):
    count = 0
    # Iterate over the list from the second element to the second-to-last element
    for i in range(1, len(lst) - 1):
        # Check if the current element is smaller than both neighbors
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            count += 1
    return count

# Reads lists until EOF 

def main():
    # Loop over each line of input from standard input 
    for line in sys.stdin:
        # Split the line into a list of strings, convert each to an integer, and store them in 'numbers'
        numbers = [int(number) for number in line.split()]
    
        # Call the function 'count_of_local_minimums' with 'numbers' as an arguments
        print(count_of_local_minimums(numbers))

# Reads n lists  

def main():
    n = int(input("Enter the number of lines: "))

    # Loop over 'n' lines of input
    for i in range(n):
        # Read a line of input
        line = input("Enter numbers separated by spaces: ")
        # Split the line into a list of strings, convert each to an integer, and store them in 'numbers'
        numbers = [int(number) for number in line.split()]
        print(count_of_local_minimums(numbers))

# Reads lists until empty line

def main():
    # Read the first line of input
    line = input("Enter numbers separated by spaces (leave blank to stop): ")
    # Continue processing lines until an empty line is entered
    while line != '':
        # Split the line into a list of integers
        numbers = [int(number) for number in line.split()]
        print(count_of_local_minimums(numbers))
        
        # Read the next line of input
        line = input("Enter numbers separated by spaces (leave blank to stop): ")


# Run the main function
if __name__ == "__main__":
    main()