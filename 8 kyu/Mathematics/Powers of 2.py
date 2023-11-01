def powers_of_two(n: int) -> list:
    return [2 ** i for i in range(n + 1)]


print(powers_of_two(2))     # -> [1, 2, 4]
print(powers_of_two(4))     # -> [1, 2, 4, 8, 16]
