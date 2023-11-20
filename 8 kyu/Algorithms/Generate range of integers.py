def generate_range(low: int, high: int, step: int) -> list:
    return list(range(low, high + 1, step))


print(generate_range(1, 10, 1))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(generate_range(1, 7, 2))  # [1, 3, 5, 7]
