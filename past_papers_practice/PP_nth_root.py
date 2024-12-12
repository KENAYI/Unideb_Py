import sys

def apply_n_root(nums, n):
    return [num ** (1/n) for num in nums]

def main():
    n = int(sys.argv[1])
    
    nums = [float(num) for num in sys.argv[2:]]
    
    roots = apply_n_root
    
    output = ", ".join(f"{root:.3f}" for root in roots)
    print(output)

if __name__ == "__main__":
    main()