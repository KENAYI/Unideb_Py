import sys

def sum_rec(n):
    if n == 3:
        return 54
    else:
        return (n * n) * ((n * n) - 3) + sum_rec(n - 1)

def main():
    n = int(input('n= '))
    
    while n !=0:
        print('sum= ', sum_rec(n))
        n = int(input('n= '))

if __name__ == "__main__":
    main()