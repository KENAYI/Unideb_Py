import sys

def apply_exponent(v, nums):
    return [(num ** v) for num in nums]

def main():
    
    exp = int(sys.argv[1])
    
    nums = [float(num) for num in sys.argv[2:]]

    exponents = apply_exponent(exp, nums)

    #  Sorting
    nums_sorted = ', '.join(f"{exp:.3f}" for exp in exponents)
    print(nums_sorted)

if  __name__ == "__main__":
    main()