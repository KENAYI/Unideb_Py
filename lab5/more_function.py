import random

def gen_random_list() -> list:
    random_list = [random.randint(1, 100) for _ in range(10)]
    return random_list

def get_min_element(l: list) -> int:
    return min(l)

def get_max_element(l: list) -> int:
    return l.index(max(l))

def count_even_elements(lst):
    return sum(1 for x in lst if x % 2 == 0)

def prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(l: list) -> int:
    return sum(1 for x in l if prime(x))

def main():
    rl = gen_random_list()
    print(rl)
    print(get_min_element(rl))
    print(get_max_element(rl))
    print(count_even_elements(rl))
    print(count_primes(rl))

if __name__ == '__main__':
    main()