# Checks for palindrome list of integers

def is_palindrome(lst):
    return lst == lst[::-1]  # Check if the list is the same forwards and backwards

def main():
    print("Enter lists of numbers: \n")
    while True:
        try:
            # Read a line of input
            line = input().strip()
            if not line:  # Stop if an empty line is encountered
                break
            
            # Convert the line to a list of integers
            lst = list(map(int, line.split()))
            
            # Call the function to check if the list is a palindrome
            result = is_palindrome(lst)
            
            # Print the result for the current list
            print(result)

        except EOFError:
            break  # End of input reached

# Run the main function
if __name__ == "__main__":
    main()
