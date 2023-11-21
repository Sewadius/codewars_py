def is_triangle(a: int, b: int, c: int) -> bool:
    sides = sorted([a, b, c])
    return sides[0] + sides[1] > sides[2]


print(is_triangle(1, 2, 2))     # -> True
print(is_triangle(7, 2, 2))     # -> False
