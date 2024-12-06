import sys

# Function to count the number of local maximums
def count_of_local_maximums() -> int:
    # Convert command line arguments (excluding the script name) to integers
    numbers = [int(s) for s in sys.argv[1:]]
    
    # Initialize the count of local maximums
    count = 0
    
    # Loop through the numbers (except the first and last)
    for i in range(len(numbers) - 2):
        # Check if the current number is a local maximum
        if numbers[i] < numbers[i + 1] > numbers[i + 2]:
            count += 1  # Increment the count if it's a local maximum
    
    # Return the final count
    return count

# Main function that calls count_of_local_maximums and prints the result
def main():
    print(count_of_local_maximums())  # Output the count of local maximums

# Ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
