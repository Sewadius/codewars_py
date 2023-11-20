def find_short(s: str) -> int:
    return min(len(word) for word in s.split())


print(find_short('bitcoin take over the world'))        # -> 3
print(find_short('i want to travel the world'))         # -> 1
