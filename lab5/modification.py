def modify(func):
    # Modify the first element of the list (mutable object)
    func[0] = 5

# Create a list, 'original', that will be passed to the function
original = [1]

# Call 'modify' function with 'original' as argument
modify(original)

# Print the modified 'original' list
print(original)  # The output will be [2]
