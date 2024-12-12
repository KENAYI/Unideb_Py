import sys

def sum_rec(n):
    if n == 3:
        return 54
    else:
        return int((n * n) * ((n * n) - 3)) + sum_rec(n - 1)

def main():
    line = []
    while True:
        n = int(input('n= '))
        
        if n == 0:
            break
        
        sums = sum_rec(n)
        line.append(sums)
        
    sort = ", ".join(str(sums) for sums in line)
    print(sort)        


if __name__ == "__main__":
    main()