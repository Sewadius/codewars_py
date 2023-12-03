def move(position: int, roll: int) -> int:
    return position + 2 * roll


print(move(0, 4))       # -> 8
print(move(2, 5))       # -> 12
