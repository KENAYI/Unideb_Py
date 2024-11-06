# Start an infinite loop to continually accept input
while True:
    try:
        # Take a string input from the user
        s = input()

        # Initialize an empty string to store the result
        r = ''

        # Loop through each character in the input string
        for c in s:
            # If the character is not a vowel (ignoring case), add it to 'r'
            if c.lower() not in "aeiou":
                r = r + c

        # Print the result after removing vowels from the input string
        print(r)
    
    # If the user presses CTRL+D (EOF), break out of the loop
    except EOFError:
        break
