import sys

def sum_rec(n):
    if n == 2:
        return -1
    else:
        return int((0.5 * (n**3 - 5*n))) + sum_rec(n-1)
    
def main():
    line =[]
    while True: 
        n = int(input("n = "))
        
        if n == 0:
            break
        
        sums = sum_rec(n)
        line.append(sums)
        
    sums_sort = ", ".join(str(sums) for sums in line)
    print(sums_sort)


if __name__ == "__main__":
    main()