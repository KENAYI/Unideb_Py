import random  

# Initialize two empty sets
s1 = set()
s2 = set()

# Get the desired sizes of the two sets from user input
n = int(input("n = "))  # Number of unique random integers in set s1
m = int(input("m = "))  # Number of unique random integers in set s2

# Populate set s1 with `n` unique random integers between 1 and 20
while len(s1) < n:  
    s1.add(random.randint(1, 20))  # Add a random integer to the set

# Populate set s2 with `m` unique random integers between 1 and 20
while len(s2) < m:
    s2.add(random.randint(1, 20))  # Add a random integer to the set

# Display the generated sets
print(s1)  
print(s2)  

# Perform and display results of set operations

# Combine elements from both sets without duplicates
print("Union =", s1.union(s2))  
# Elements common to both sets
print("Intersection =", s1.intersection(s2))
# Elements in s1 but not in s2  
print("Difference =", s1.difference(s2))  
# Elements in either set but not both
print("Symmetric difference =", s1.symmetric_difference(s2))  
