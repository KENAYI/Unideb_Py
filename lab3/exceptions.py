# Infinite loop to continuously accept input and handle different exceptions
while True:
    try:
        # Take input from the user and try to convert it to an integer
        n = int(input())
        
        # Perform division by the input number and print the result
        print(2 / n)
    
    # Catch if the input is not an integer (e.g., alphabetic characters)
    except ValueError:
        print('Error! Alphabetic character!')
    
    # Catch division by zero errors
    except ZeroDivisionError:
        print('Error! Division by zero!')
    
    # Break out of the loop if an EOF (End-of-File) is encountered (e.g., CTRL+D)
    except EOFError:  # CTRL+D
        break
    
    # This block is always executed, regardless of whether an exception occurred
    finally:
        print('Always executed!')
