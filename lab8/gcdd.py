import sys

def gcd(a:int, b:int) -> int:
    while a != b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

def main():
    with open(sys.argv[1]) as file:
        for line in file:
            nums = line.strip().split()
            num = int(nums[0])
            for i in range(1, len(nums)):
                print(num)

if __name__ == '__main__':
    main()