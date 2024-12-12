import sys

# Dictionary to store the total price of clothes by type
clothes = {}

def main():
    # Check if the correct number of command-line arguments is provided
    # if len(sys.argv) != 2:
    #     return print("Invalid input!")
    
    # Get the filename from the command-line arguments
    filename = sys.argv[1]
    
    # Open the file for reading
    with open(filename, 'r') as file:
        # Read each line from the file
        for line in file:
            # Split the line into clothing type, brand, color, and price
            clothing_type, brand, color, price = line.strip('\n').split(';')

            # Add the price to the total for the clothing type
            if clothing_type in clothes:
                clothes[clothing_type] += int(price)
            else:
                clothes[clothing_type] = int(price)

# Sort the clothes dictionary by total price (descending) and then alphabetically by type
clothes_sorted = sorted(clothes.items(), key=lambda x: (-x[1], x[0]))

# Print the sorted clothing types with their total prices
for key, value in clothes_sorted:
    print(f'{key} ({value:.2f} EUR)')

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
