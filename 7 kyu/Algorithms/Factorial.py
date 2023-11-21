from math import factorial as f


def factorial(n: int) -> int:
    if n < 0 or n > 12:
        raise ValueError
    return f(n)


print(factorial(0))     # -> 1
print(factorial(3))     # -> 6
