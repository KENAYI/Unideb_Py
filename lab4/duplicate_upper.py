# Take the first input string from the user
s = input()

# Continue processing input as long as it's not 'END'
while s != 'END':
    # Initialize an empty string to store the result
    r = ''
    
    # Loop through each character in the string 's'
    for c in s:
        # If the character is an uppercase letter, repeat it twice
        if c.isupper():
            r += c * 2
        # Otherwise, just add the character as it is
        else:
            r += c
    
    # Print the modified string 'r'
    print(r)

    # Take the next input string from the user
    s = input()
