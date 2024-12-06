import sys

# Dictionary to store the total count of drivers' data
drivers = {}

# Open the file passed as the first command-line argument
with open(sys.argv[1]) as file:
    # Iterate through each line in the file
    for line in file:
        # Strip newline characters and split by semicolon
        data = line.strip("\n").split(";")
        
        # Check if the driver (data[0]) is already in the dictionary
        if data[0] in drivers:
            # If the driver exists, add the count to their total
            drivers[data[0]] += int(data[2])
        else:
            # If the driver does not exist, initialize their count
            drivers[data[0]] = int(data[2])

# Sort the dictionary items first by count (in descending order), 
# then by driver name (in ascending order) and print each driver
for key, value in sorted(drivers.items(), 
                            key=lambda x: (-x[1], x[0])):
    print(key)
