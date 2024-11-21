import sys
import math

def count_of_squares(nums: list[int]) -> int:
    count = 0  
    for num in nums:  
        # Check if the number is a perfect square
        if num == int(math.sqrt(num) ** 2):
            count += 1  
    return count  

def main():
    # Read lines of input from standard input 
    for line in sys.stdin:
        nums = line.split(" ")  
        lists = []  
        for num in nums:  # Convert each string to an integer
            lists.append(int(num))
        
        print(count_of_squares(lists))
        
def main1():
    n = int(input('Enter number of entries: '))
    
    for i in range(n):
        nums = n.split(" ")  
        lists = []  
        for num in nums:  # Convert each string to an integer
            lists.append(int(num))
        
        print(count_of_squares(lists))
        
def main2():
    for line in sys.stdin:
        if line.strip() == "":
            break
        nums = line.split(" ")
        lists = []
        for num in nums:
            lists.append(int(num))
        print(count_of_squares(lists))

if __name__ == '__main__':
    main2()