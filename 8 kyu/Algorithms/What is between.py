def between(a: int, b: int) -> list:
    return [*range(a, b + 1)]


print(between(1, 4))    # -> [1, 2, 3, 4]
print(between(-2, 2))      # -> [-2, -1, 0, 1, 2]
