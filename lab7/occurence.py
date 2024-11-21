# Initialize an empty dictionary to store word occurrences
occurrence = {}

# Take the first word input
word = input()

# Keep accepting words until the input is an empty string (""), signaling the end
while word != "":
    if word in occurrence:  # Check if the word already exists in the dictionary
        occurrence[word] += 1  # Increment the count of the existing word
    else:
        occurrence[word] = 1  # If the word is not found, add it to the dictionary with count 1
    
    # Take the next word input
    word = input()

# Iterate over the dictionary to print the word and its occurrence count
for key, value in occurrence.items():
    print(f"{key}: {value}")
