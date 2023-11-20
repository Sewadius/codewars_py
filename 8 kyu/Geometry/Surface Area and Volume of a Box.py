def get_size(w: int, h: int, d: int) -> list:
    area = 2 * w * h + 2 * w * d + 2 * h * d
    volume = w * h * d
    return [area, volume]


print(get_size(4, 2, 6))  # [88, 48]
print(get_size(1, 2, 2))  # [16, 4]
