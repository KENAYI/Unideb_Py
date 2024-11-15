# Recursive function to calculate the factorial of a number

def factr(n: int) -> int:
    # Base case: factorial of 1 is 1
    if n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factr(n - 1)

# Recursive function to calculate factorial using a single-line ternary expression

def factr1(n: int) -> int:
    # Use ternary operator for base and recursive case
    return 1 if n == 1 else n * factr1(n - 1)

# Recursive function to calculate power of a number

def pow(n: int, exp: int) -> int:
    # Base case: any number to the power of 0 is 1
    if exp == 0:
        return 1
    # Recursive case: n * power of (n, exp-1)
    else:
        return n * pow(n, exp - 1)

# Recursive function to calculate power using a single-line expression

def pow1(n: int, exp: int) -> int:
    # Use ternary operator for base and recursive case
    return n if exp == 1 else n * pow1(n, exp - 1)

# Main function to take user input and demonstrate the recursive functions

def main():
    n = int(input("n= "))
    exp = int(input("exp ="))

    print('Fact = ', factr(n))
    print('Fact= ', factr1(n))
    
    print('Pow= ', pow(n, exp))
    print('Pow= ', pow1(n, exp))

if __name__ == "__main__":
    main()
