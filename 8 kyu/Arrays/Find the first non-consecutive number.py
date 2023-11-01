def first_non_consecutive(arr: list) -> int:
    for i, el in enumerate(arr):
        if i < len(arr) - 1 and arr[i + 1] - el != 1:
            return arr[i + 1]
    return None


print(first_non_consecutive([1,2,3,4,6,7,8]))   # -> 6
print(first_non_consecutive([31, 32]))          # -> None
print(first_non_consecutive([-5,-4,-3,-1]))     # -> -1
