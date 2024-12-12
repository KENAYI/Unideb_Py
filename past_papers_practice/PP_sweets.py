import sys

# Dictionary to store the count of students for each subject
students = {}

# Read each line from standard input
for line in sys.stdin:
    # Split the line into student name and subjects
    data = line.strip().split(':')
    
    # Extract the student name
    student = data[0]
    
    # Extract the list of subjects
    subjects = data[1].split(',')
    
    # Count the number of students for each subject
    for i in subjects:
        if i in students:
            students[i] += 1
        else:
            students[i] = 1

# Sort the subjects by the number of students (descending) and then alphabetically
students_sorted = sorted(students.items(), key=lambda x: (-x[1], x[0]))

# Print the sorted subjects with the number of students
for key, value in students_sorted:
    print(f"{key}:{value} student(s)")
