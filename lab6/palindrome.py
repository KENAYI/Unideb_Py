import sys

def is_palindrome(numbers: list[int]) -> bool:
    # Compare the list with its reversed version
    if numbers == numbers[::-1]:
        return True
    else:
        return False

# Reads lists until EOF 

def main():
    # Loop over each line of input from standard input
    for line in sys.stdin:
        # Convert the space-separated numbers in the line into a list of integers
        numbers = [int(number) for number in line.split()]

        print(is_palindrome(numbers))

# Reads n test cases

def main():
    # Get the number of lines of input
    n = int(input("Enter the number of lines: "))

    # Loop through 'n' lines
    for i in range(n):
        # Read a line of input
        line = input("Enter numbers separated by spaces: ")
        
        # Convert the space-separated numbers into a list of integers
        numbers = [int(number) for number in line.split()]
        
        # Call the function 'is_palindrom' to check if the list is a palindrome
        # (Ensure that 'is_palindrom' is defined in your code)
        print(is_palindrome(numbers))

# Reads until an empty file

def main():
    # Read the first line of input
    line = input("Enter numbers separated by spaces (leave blank to stop): ")
    # Continue processing lines until an empty line is entered
    while line != '':
        # Convert the space-separated numbers into a list of integers
        numbers = [int(number) for number in line.split()]
        print(is_palindrome(numbers))
        # Read the next line of input
        line = input("Enter numbers separated by spaces (leave blank to stop): ")

if __name__ == "__main__":
    main()