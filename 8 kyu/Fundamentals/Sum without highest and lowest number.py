def sum_array(arr: list) -> int:
    if not arr or len(arr) == 1:
        return 0
    return sum(arr) - max(arr) - min(arr)


print(sum_array([]))                    # -> 0
print(sum_array(None))                  # -> 0
print(sum_array([6, 2, 1, 8, 10]))      # -> 16
print(sum_array([-3]))                  # -> 0
