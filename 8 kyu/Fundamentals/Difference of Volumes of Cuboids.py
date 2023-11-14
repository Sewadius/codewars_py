def find_difference(a: list, b: list) -> int:
    volume_1, volume_2 = [1] * 2
    for el in a:
        volume_1 *= el
    for el in b:
        volume_2 *= el
    return max(volume_1, volume_2) - min(volume_1, volume_2)


print(find_difference([3, 2, 5], [1, 4, 4]))        # -> 14
print(find_difference([9, 7, 2], [5, 2, 2]))        # -> 106
