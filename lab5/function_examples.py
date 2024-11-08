# (1) Functions without parameters

def table(base: int) -> None:
    """
    Prints the multiplication table of the given base up to 10 times the base.

    Parameters:
    base (int): The base number for the multiplication table.
    """
    # Start the multiplier at 1
    n = 1

    # Loop to print the multiplication table up to 10 times the base
    while n < 11:
        # Print the result of base * n with a space, staying on the same line
        print(n * base, end=" ")
        
        # Increment n to move to the next multiple
        n = n + 1

# Call the function with 13 as the base to print the table of 13
table(13)


# (2) Multiple parameter function

def table(base: int, start: int, end: int) -> None:
    """
    Prints a specified range of the multiplication table for a given base.

    Parameters:
    base (int): The base number for the multiplication table.
    start (int): The starting multiplier for the table.
    end (int): The ending multiplier for the table.
    """
    # Display header for the table
    print("Part of the multiplication table of {}:".format(base))

    # Initialize the multiplier at the starting value
    n = start

    # Loop to print each line in the specified range of the multiplication table
    while n <= end:
        # Print the formatted multiplication statement for the current multiplier
        print("{0} x {1} = {2}".format(n, base, n * base))

        # Increment n to move to the next multiplier
        n = n + 1

# Call the function with different bases and ranges
table(2, 1, 10)  # Prints the table for 2 from 2*1 to 2*10
table(8, 10, 20) # Prints the table for 8 from 8*10 to 8*20


# (3) Global var

def increase() -> None:
    """
    Increases the global variable 'a' by 1 and prints the updated value.
    """
    global a  # Declare 'a' as global to modify it within the function
    a = a + 1  # Increment the global variable 'a' by 1
    print(a)  # Print the updated value of 'a'

# Initialize the global variable 'a'
a = 15

# Call the function to increase 'a' and print the result
increase()


# (4) Optional Parameters

def quadrilateral(a: int, b: int = 0) -> int:
    """
    Calculates the area of a square or rectangle based on the given dimensions.

    Parameters:
    a (int): The length of one side (or length of a rectangle).
    b (int, optional): The length of the other side. Defaults to 0.
                        If b is 0, the shape is considered a square (b = a).

    Returns:
    int: The area of the square or rectangle.
    """
    # If only one dimension is provided, assume a square
    if b == 0:
        b = a  # Set b to a for a square
    
    # Return the area
    return a * b

# Examples of function usage
print('Area of square:', quadrilateral(10))         # Square with side length 10
print('Area of rectangle:', quadrilateral(10, 12))  # Rectangle with length 10 and width 12
#print('Area of rectangle:', quadrilateral(b=2, a=12))  # Rectangle with length 12 and width 2 (using keyword arguments)

