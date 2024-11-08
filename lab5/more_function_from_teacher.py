import random  # Import random for generating random numbers
import math    # Import math for using sqrt in prime check

# Function to generate 10 random integers between 1 and 100
def generate(li: list) -> None:
    for i in range(10):
        li.append(random.randint(1, 100))

# Function to check if a number is prime
def isprim(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    d = 2
    while d <= math.sqrt(n):
        if n % d == 0:
            return False
        d += 1
    return True

# Function to count the number of prime numbers in the list
def prime_numbers(li: list) -> int:
    prime = 0
    for i in range(len(li)):
        if isprim(li[i]):
            prime += 1
    return prime

# Function to find the minimum value in the list
def minimum_value(li: list) -> int:
    min_value = li[0]
    for i in range(1, len(li)):
        if li[i] < min_value:
            min_value = li[i]
    return min_value

# Function to find the index of the maximum value in the list
def maximum_index(li: list) -> int:
    maxi = 0
    for i in range(1, len(li)):
        if li[i] > li[maxi]:
            maxi = i
    return maxi

# Function to count the number of even numbers in the list
def evens(li: list) -> int:
    even_count = 0
    for i in range(len(li)):
        if li[i] % 2 == 0:
            even_count += 1
    return even_count

# Main function to execute all the tasks
def main():
    li = []  # Create an empty list
    generate(li)  # Generate random numbers and append to the list
    print("Generated list:", li)  # Print the generated list

    # Print results for various calculations
    print("Minimum value =", minimum_value(li))
    print("Maximum index =", maximum_index(li))
    print("Number of evens =", evens(li))
    print("Number of primes =", prime_numbers(li))

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
