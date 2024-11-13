# Count local minimums from given lists

def count_of_local_minimums(lst):
    count = 0
    # Iterate over the list from the second element to the second-to-last element
    for i in range(1, len(lst) - 1):
        # Check if the current element is smaller than both neighbors
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            count += 1
    return count


def main():
    print("Enter lists of numbers: \n")
    while True:
        try:
            # Read a line of input
            line = input().strip()
            if not line:  # Stop if an empty line is encountered
                break
            
            # Convert the line to a list of integers
            lst = list(map(int, line.split()))
            
            # Call the function to get the count of local minimums
            result = count_of_local_minimums(lst)
            
            # Print the result for the current list
            print(f"Local minimums count: {result}")

        except EOFError:
            break  # End of input reached

# Run the main function
if __name__ == "__main__":
    main()