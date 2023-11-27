def quadrant(x: int, y: int) -> int:
    if x > 0 and y > 0:
        return 1
    if x < 0:
        if y > 0:
            return 2
        if y < 0:
            return 3
    if x > 0 > y:
        return 4


print(quadrant(3, 5))       # -> 1
print(quadrant(-1, -9))           # -> 3
