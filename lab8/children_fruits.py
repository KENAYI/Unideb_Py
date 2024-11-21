# Initialize an empty dictionary to store the fruits liked by each child
children_fruits = {}

# Read input line by line until EOF
while True:
    try:
        line = input().strip()
        if not line:  # Handle empty input 
            break
        # Split the line at ':' to get the fruit name and the list of children
        fruit, children = line.split(':')
        
        # Split the children names by commas
        child_list = children.split(',')
        
        # For each child, add the fruit to their set of liked fruits
        for child in child_list:
            if child not in children_fruits:
                children_fruits[child] = set()
            children_fruits[child].add(fruit)
    
    except EOFError:
        break

# Sort the dictionary by child names (lexicographically)
sorted_children = sorted(children_fruits.items())

# Print the result
for child, fruits in sorted_children:
    # The number of different fruits the child likes is the length of the set for that child
    print(f'{child}: {len(fruits)}')
