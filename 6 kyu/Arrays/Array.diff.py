def array_diff(a: list, b: list) -> list:
    return [i for i in a if i not in b]


print(array_diff([1, 2], [1]))          # -> [2]
print(array_diff([1, 2, 3], [1, 2]))    # -> [3]
