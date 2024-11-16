import sys

def delete_even_digits(nums: str)-> str:
    even_digits = "2468"
    result = ''.join(char for char in nums if char not in even_digits)
    
    return result

def main():
    for line in sys.stdin:
        print(delete_even_digits(line.strip()))

# For n cases

def main1():
    n = int(input('Enter number of entries: '))
    for line in range(n):
        line = input()
        print(delete_even_digits(line.strip()))

def main2():
    line = input('Enter string (leave empty to end): ')
    
    while line != '':
        print(delete_even_digits(line.strip()))
        line = input('Enter string (leave empty to end): ')

if __name__ == "__main__":
    main2()