import sys
import math


def count_odds() -> int:
    count = 0
    for n in sys.argv[2:]:
        if int(n) % 2 == 1:
            count += 1
    return count

def is_prime(n: int):
    if n == 0 or n == 1:
        return False
    d = 2
    while d <= math.sqrt(n):
        if n % d == 0:
            return False
        d = d + 1
    return True


def count_primes() -> int:
    count = 0
    for num in sys.argv[2:]:
        if is_prime(int(num)):
            count += 1
    return count

def main():
    print(count_odds())
    print(count_primes())

if __name__ == "__main__":
    main()