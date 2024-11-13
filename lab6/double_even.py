# Reads in a list of characters and doubles the num of even integers in the list

def double_even_digits(s):
    result = ""
    for char in s:
        # Check if the character is a digit and if it is even
        if char.isdigit() and int(char) % 2 == 0:
            result += char * 2  # Duplicate the even digit
        else:
            result += char  # Keep other characters as they are
    return result

def main():
    while True:
        try:
            # Prompt the user to enter a string
            line = input("Input string: \n").strip()
            if not line:  # Stop if an empty string is encountered
                break
            
            # Call the function to get the transformed string
            result = double_even_digits(line)
            
            # Print the result for the current string
            print(result)

        except EOFError:
            break  # End of input reached

# Run the main function
if __name__ == "__main__":
    main()