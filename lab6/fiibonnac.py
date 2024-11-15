# Recursive function to calculate the nth Fibonacci number

def fibonacci(n: int) -> int:
    # Base case: Fibonacci of 0 is 0
    if n == 0:
        return 0
    # Base case: Fibonacci of 1 is 1
    if n == 1:
        return 1
    # Recursive case: Fibonacci of n is the sum of the two previous Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# OR

# Iterative function to calculate the nth Fibonacci number
def fibonacci(n: int) -> int:
    # Initialize the first two Fibonacci numbers
    f1 = 0  # F(0)
    f2 = 1  # F(1)
    
    # Handle the base cases directly
    if n == 0:
        return 0  
    elif n == 1:
        return 1 
    else:
        # Calculate Fibonacci iteratively for n > 1
        for i in range(1, n):  # Loop from 1 to n-1
            f3 = f2 + f1  # Calculate the next Fibonacci number
            f1 = f2       # Update f1 to the previous f2
            f2 = f3       # Update f2 to the new Fibonacci number
        return f3  # Return the nth Fibonacci number

# OR

# Function to generate the first n Fibonacci numbers as a list
def fibonacci1(n: int) -> list[int]:
    # Initialize the result list with the first two Fibonacci numbers
    f = [0, 1]
    
    # Generate the Fibonacci numbers starting from index 2 up to n-1
    for i in range(2, n):
        # Append the sum of the two previous numbers to the list
        f.append(f[i - 1] + f[i - 2])
    
    # Return the complete Fibonacci sequence as a list
    return f


# Main function to read input and print Fibonacci series
def main():
    n = int(input("n = "))
    # Loop to calculate and print each Fibonacci term up to n-1
    for i in range(n):
        # Print Fibonacci numbers on the same line, separated by spaces
        print(fibonacci(i), end=' ')  

    print(*fibonacci1(n))  # Unpack the list to print space-separated values

if __name__ == "__main__":
    main()