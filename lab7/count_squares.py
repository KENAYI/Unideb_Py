import sys
import math

def count_of_squares(nums: list[int]) -> int:
    count = 0
    # Iterate through each number in list
    for num in nums:
        # Only non-negative numbers
        if num >= 0:
            sqrt = math.isqrt(num) # Integer square root
            if sqrt * sqrt == num: # Check that it is perfect square
                count += 1 
    return count

def main():
    for line in sys.stdin:
        nums = [int(num) for num in line.split()]
        
        print(count_of_squares(nums))
        
def main1():
    n = int(input('Enter number of entries: '))
    
    for i in range(n):
        line = input('Enter numbers separated by spaces: ')
        nums = [int(num) for num in line.split()]
        
        print(count_of_squares(nums))
        
def main2():
    line = input('Enter numbers separated by spaces (leave blank to stop): ')
    
    while line != '':
        nums = [int(num) for num in line.split()]
        print(count_of_squares(nums))
        line = input('Enter numbers separated by spaces (leave blank to stop): ')

if __name__ == '__main__':
    main2()