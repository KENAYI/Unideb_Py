# Script takes two floating-point values and calculates the hypotenuse of a triangle
import math
import sys

# Function to calculate the hypotenuse using the Pythagorean theorem
def pythagorean(a: float, b: float) -> float:
    hyp = math.sqrt((a**2) + (b**2))  # Calculate the hypotenuse
    return hyp

# Main function to read input and calculate hypotenuse
def main():
    for line in sys.stdin:
        # Split the input into two numbers and unpack them
        nums = line.split()
        a = float(nums[0])
        b = float(nums[1])
        # Calculate and print the hypotenuse
        print(f"Hypotenuse: {pythagorean(a, b):.2f}")

def main1():
    n = int(input("How many values: "))
    for i in range(n):
        nums = input("Enter values: ").split()
        a = float(nums[0])
        b = float(nums[1])
        # Calculate and print the hypotenuse
        print(f"Hypotenuse: {pythagorean(a, b):.2f}")

def main2():
    for line in sys.stdin:
        if line.strip() == "":
            break
        nums = line.split()
        a = float(nums[0])
        b = float(nums[1])
        # Calculate and print the hypotenuse
        print(f"Hypotenuse: {pythagorean(a, b):.2f}")

if __name__ == "__main__":
    main2()