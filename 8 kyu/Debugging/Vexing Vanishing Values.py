def mul_by_n(lst: list, n: int) -> list:
    return [i * n for i in lst]


print(mul_by_n([1, 2, 3], 4))       # -> [4, 8, 12]
print(mul_by_n([9, 1], 9))          # -> [81, 9]
