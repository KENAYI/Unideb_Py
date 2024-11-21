# Initialize an empty dictionary to store the data for each monkey
monkey = {}

# Ask the user how many entries they want to input
n = int(input("Enter the number of entries: "))

# Iterate through the specified number of entries
for _ in range(n):
    # Input line from the user
    line = input("Enter monkey and count: ").strip()

    # Split the line into two parts using ';' as the delimiter
    data = line.split(';')
        
    # Add the monkey and count to the dictionary
    if data[0] in monkey:
        monkey[data[0]] += int(data[1])
    else:
        monkey[data[0]] = int(data[1])

# After processing all input, sort the dictionary by keys (monkey names)
# Iterate over the sorted dictionary and print each key-value pair
print("\nSorted Monkey List:")
for key, value in sorted(monkey.items()):
    print(f'{key}: {value}')
