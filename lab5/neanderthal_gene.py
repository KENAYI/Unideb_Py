import sys

# Function to check if there exists a monotonic subsequence of length 3
def contains_neanderthal_gene(sequence):
    # Loop through the sequence to check for strictly monotonic subsequences
    for i in range(len(sequence) - 2):  # We need at least three elements
        # Check if the sequence is strictly increasing
        if sequence[i] < sequence[i+1] < sequence[i+2]:
            return True
        # Check if the sequence is strictly decreasing
        if sequence[i] > sequence[i+1] > sequence[i+2]:
            return True
    return False

# Reading input until EOF
for line in sys.stdin:
    # Convert the input line into a list of integers
    sequence = list(map(int, line.split()))
    
    # Check if the sequence contains a Neanderthal gene
    if contains_neanderthal_gene(sequence):
        print("YES")
    else:
        print("NO")
