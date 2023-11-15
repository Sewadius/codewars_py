def odd_count(n: int) -> int:
    return len(range(1, n, 2))


print(odd_count(7))     # -> 3
print(odd_count(15))    # -> 7
