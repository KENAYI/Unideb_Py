import random  # Import the random module to generate random numbers

# Initialize two empty sets 
even = set()
odd = set()

n = int(input("n = "))  # Number of unique even integers to generate
m = int(input("m = "))  # Number of unique odd integers to generate

# Populate the 'even' set with `n` unique even numbers
while len(even) < n:  
    num = random.randint(1, 20)  
    if num % 2 == 0:  # Check if the number is even
        even.add(num)  

# Populate the 'odd' set with `m` unique odd numbers
while len(odd) < m:
    num = random.randint(1, 20) 
    if num % 2 == 1:  # Check if the number is odd
        odd.add(num) 

# Display the generated sets
print(even)  
print(odd)  

print("Union =", even.union(odd))  # Combine elements from both sets without duplicates