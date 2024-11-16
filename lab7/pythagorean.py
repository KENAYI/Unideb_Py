# Script takes two floating-point values and calculates the hypotenuse of a triangle
import math
import sys

# Function to calculate the hypotenuse using the Pythagorean theorem
def pythagorean(a: float, b: float) -> float:
    hyp = math.sqrt((a * a) + (b * b))  # Calculate the hypotenuse
    return hyp

# Main function to read input and calculate hypotenuse
def main():
    for line in sys.stdin:
        # Split the input into two numbers and unpack them
        nums = [float(num) for num in line.split()]
        
        if len(nums) != 2:  # Ensure exactly two numbers are provided
            print("Error: Please provide exactly two numbers.")
            continue

        a, b = nums  # Unpack the two sides

        # Calculate and print the hypotenuse
        print(f"Hypotenuse: {pythagorean(a, b):.2f}")

if __name__ == "__main__":
    main()
