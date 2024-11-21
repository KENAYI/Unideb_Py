# Initialize a dictionary to represent a shopping list
shoppinglist = dict([
    ("apple", 2),  # "apple" is the key, and 2 is the quantity
    ("pear", 1),   # "pear" is the key, and 1 is the quantity
    ("peach", 5),  # "peach" is the key, and 5 is the quantity
])

# Print the initial shopping list
print(shoppinglist)
# Output: {'apple': 2, 'pear': 1, 'peach': 5}

# Access and print the value associated with the key "apple"
print(shoppinglist["apple"])  
# Output: 2

# Check if the key "apple" exists in the dictionary
print("apple" in shoppinglist)  
# Returns boolean

# Remove the key "apple" and its associated value from the dictionary
del shoppinglist["apple"]

# Add a new key-value pair to the dictionary
shoppinglist["plum"] = 7  

# Print the updated shopping list, with plum now
print(shoppinglist)

# Try to access a key that does not exist in the dictionary
try:
    print(shoppinglist["papaja"])  
except KeyError as e: 
    print("Not in it!")  

# Iterate over the dictionary to print each key
for key in shoppinglist:  # Access dictionary keys
    print(key)

# Iterate over the dictionary to print each value
for value in shoppinglist.values():  # Access dictionary values
    print(value)

# Calculate and print the sum of all values in the dictionary
print("Sum:", sum(shoppinglist.values()))

# Iterate over the dictionary to print each key-value pair
for key, value in shoppinglist.items():  # Access both keys and values
    print(f"{key}: {value} kg")