# Take an input for the score (point)
point = int(input('Enter grade: '))

# Keep checking the score as long as it is greater than or equal to 0
while point >= 0:
    # If the score is 80 or higher, print "excellent"
    if point >= 80:
        print("excellent")
    # If the score is 70 or higher, but less than 80, print "good"
    elif point >= 70:
        print("good")
    # If the score is 60 or higher, but less than 70, print "average"
    elif point >= 60:
        print("average")
    # If the score is 50 or higher, but less than 60, print "satisfactory"
    elif point >= 50:
        print("satisfactory")
    # If the score is less than 50, print "insufficient"
    else:
        print("insufficient")
    
    # Ask for the next score input
    point = int(input('Enter another grade: '))
