# Function to calculate the sum of the first n natural numbers recursively
def sum(n: int) -> int:
    # Base case: sum of the first natural number is 1
    if n == 1:
        return 1
    # Recursive case: sum of n is n + sum of (n-1)
    else:
        return n + sum(n - 1)

# Function to calculate the sum using a single-line ternary operator
def sum1(n: int) -> int:
    # Base case and recursive case handled in one line
    return 1 if n == 1 else n + sum1(n - 1)

# Function to calculate the sum of squares of the first n natural numbers
def sum2(n: int) -> int:
    # Base case: the square of 1 is 1
    if n == 1:
        return 1
    # Recursive case: sum of squares is n^2 + sum of squares of (n-1)
    else:
        return n * n + sum2(n - 1)

# Function to calculate a custom sequence sum: n^2 - 2
def sum3(n: int) -> int:
    # Base case: specific return value when n == 1
    if n == 1:
        return -1
    # Recursive case: custom formula n^2 - 2 + sum3(n-1)
    else:
        return n * n - 2 + sum3(n - 1)

# Function to calculate a custom sequence sum with specific conditions for n < 3 and n == 3
def sum4(n: int) -> int:
    # Base case: return 0 for n < 3
    if n < 3:
        return 0
    # Base case: return 7 when n == 3
    if n == 3:
        return 7
    # Recursive case: custom formula n^2 - 2 + sum4(n-1)
    else:
        return n * n - 2 + sum4(n - 1)

# Function to calculate a custom sequence sum with specific conditions for n < 4 and n == 4
def sum5(n: int) -> int:
    # Base case: return 0 for n < 4
    if n < 4:
        return 0
    # Base case: return 60 when n == 4
    if n == 4:
        return 60
    # Recursive case: custom formula n * (n^2 - 1) + sum5(n-1)
    else:
        return n * (n * n - 1) + sum5(n - 1)

# Function to calculate a custom sequence sum: n^3 - 5
def sum6(n: int) -> int:
    # Base case: return 0 for n < 2
    if n < 2:
        return 0
    # Base case: return 3 when n == 2
    if n == 2:
        return 3
    # Recursive case: custom formula n^3 - 5 + sum6(n-1)
    else:
        return n * n * n - 5 + sum6(n - 1)

# Main function to prompt user input and display results
def main():
    # Read the input value for n
    n = int(input('n= '))
    
    print('sum= ', sum(n))
    print('sum1= ', sum1(n))
    print('sum2= ', sum2(n))
    print('sum3= ', sum3(n))
    print('sum4= ', sum4(n))
    print('sum5= ', sum5(n))
    print('sum6= ', sum6(n))

# Entry point of the program
if __name__ == "__main__":
    main()
