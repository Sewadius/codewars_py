import sys


def total_bytes(obj) -> int:
    return sys.getsizeof(obj)


print(total_bytes('hello'))     # -> 54
print(total_bytes([1, 2]))      # -> 72
