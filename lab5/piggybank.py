import sys

# Initialize total savings and count of regular savers
total_savings = 0
regular_savers = 0

# Read each line of input
for line in sys.stdin:
    # Split the line by the colon to separate name and savings
    parts = line.strip().split(":")
    name = parts[0]
    savings = list(map(int, parts[1].split()))

    # Add the total savings of this child to the total savings
    total_savings += sum(savings)

    # Check if the child regularly saved at least 20 forints each time
    if all(s >= 20 for s in savings):
        regular_savers += 1

# Print the total savings
print(total_savings)
# Print the count of regular savers
print(regular_savers)
