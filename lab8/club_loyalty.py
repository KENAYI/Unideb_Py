# Read the threshold number of clubs (n) which a player has been associated with
n = int(input())

# Dictionary to store athletes and the set of clubs they've been associated with
athletes_clubs = {}

# Read input until EOF
while True:
    try:
        # Read a line of input (club and athletes)
        line = input().strip()
        
        # If line is empty, skip it
        if not line:
            continue
        
        # Split the line into club_name and the list of athlete names
        club_name, athletes = line.split(':')
        athlete_list = athletes.split(',')
        
        # For each athlete, add the club to their set of associated clubs
        for athlete in athlete_list:
            if athlete not in athletes_clubs:
                athletes_clubs[athlete] = set()
            athletes_clubs[athlete].add(club_name)
    
    except EOFError:
        break

# Filter athletes who have been associated with more than K clubs
filtered_athletes = [
    (athlete, len(clubs)) for athlete, clubs in athletes_clubs.items() if len(clubs) > K
]

# Sort athletes: first by the number of clubs (descending), then by name (lexicographically)
filtered_athletes.sort(key=lambda x: (-x[1], x[0]))

# Print the sorted list of athletes
for athlete, _ in filtered_athletes:
    print(athlete)
