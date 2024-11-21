# Read the number of subjects
n = int(input())

subjects = []

# Read each subject entry
for _ in range(n):
    line = input().strip()
    
    # Split the line into subject_code, subject_name, and credit_number
    subject_code, subject_name, credit_number = line.split(':')
    
    # Extract the semester (xx) and unique identifier (yy) from the subject_code
    _, semester, unique_id = subject_code.split('-')
    
    # Convert semester and unique_id to integers for proper sorting
    semester = int(semester)
    unique_id = int(unique_id)
    
    # Add the subject to the list as a tuple: (semester, unique_id, subject_name)
    subjects.append((semester, unique_id, subject_name))

# Sort the subjects by semester, and by unique identifier within the same semester
subjects.sort()

# Output the sorted subject names
for subject in subjects:
    print(subject[2])  # subject[2] is the subject_name
