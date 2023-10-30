def array_plus_array(arr1: list, arr2: list) -> int:
    arr1.extend(arr2)
    return sum(arr1)


print(array_plus_array([1, 2, 3], [4, 5, 6]))   # -> 21
