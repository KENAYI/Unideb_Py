# Define sets and manipulate
s1 = {"hungarian", "english", "german"}

# Define an empty set s2
s2 = set()

# Add elements to s2
s2.add("italian") 
s2.add("german")  

# Print the contents of the sets
print(s1)  
print(s2)  

print("-----------------------------------------")

# Perform various set operations

# Intersection: Elements common to both sets
print(s1.intersection(s2)) 
print(s1 & s2)             

# Union: All unique elements from both sets combined
print(s1.union(s2))        
print(s1 | s2)             

# Difference: Elements in s1 that are not in s2
print(s1.difference(s2))    
print(s1 - s2)             

# Symmetric Difference: Elements that are in either set, but not both
print(s1.symmetric_difference(s2)) 
print(s1 ^ s2)                     
