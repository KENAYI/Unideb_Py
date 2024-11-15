import sys 

# Reads in a list of characters and doubles the num of even integers in the list

def double_even_digits(s: str) -> str:
    result = ""
    for char in s:
        # Check if the character is a digit and if it is even
        if char.isdigit() and int(char) % 2 == 0:
            result += char * 2  # Duplicate the even digit
        else:
            result += char  # Keep other characters as they are
    return result

# OR

# def double_even_digits(s: str) -> str:
#     return ''.join([char * 2 if char in '02468' else char for char in s])

# Reads strings until EOF 
def main1():
    for line in sys.stdin:
        # Remove leading/trailing whitespace and process
        print(double_even_digits(line.strip()))  

# Reads n test cases
def main2():
    # Read the number of test cases 
    n = int(input("Enter number of test cases: "))  
    for i in range(n):
        line = input()  # Read each line
        print(double_even_digits(line))  

# Reads until an 'END' string is encountered
def main3():
    line = input("Enter a string (type 'END' to stop): ")  
    while line != 'END':
        print(double_even_digits(line))  
        # Continue reading lines
        line = input("Enter another string (type 'END' to stop): ") 


# Run the main function
if __name__ == "__main__":
    main3()