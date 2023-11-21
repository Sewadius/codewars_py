def sum_two_smallest_numbers(numbers: list) -> int:
    minimum = min(numbers)
    numbers.remove(minimum)
    minimum_second = min(numbers)
    return minimum + minimum_second


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))     # -> 13
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))    # -> 19
