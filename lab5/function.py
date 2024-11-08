def add(a: int, b: int) -> int:
    return a+b

def sum(n:int) -> int :
    t = 0
    for i in range(1, n+1):
        t+= i
    return t

def factorial(n: int) -> int:
    r = 1
    for i in range(n, 0, -1):
        r *= i
    return r

def power(x:int, n:int) -> int:
    r = 1
    for _ in range(n):
        r *= x
    return r

def main():
    print(add(5, 7))
    print(sum(10))
    print(factorial(5))
    print(power(5,2))

if __name__ == '__main__':
    main()