def to_binary(n: int) -> int:
    return int(bin(n)[2:])


print(to_binary(5))     # -> 101
print(to_binary(3))     # -> 11
