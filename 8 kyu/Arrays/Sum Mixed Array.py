def sum_mix(arr: list) -> int:
    return sum([int(i) for i in arr])


print(sum_mix([9, 3, '7', '3']))                        # -> 22
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))       # -> 42
