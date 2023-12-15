def count(s: str) -> dict:
    return {i: s.count(i) for i in s}


print(count('aba'))     # -> {'a': 2, 'b': 1}
print(count('aaa'))     # -> {'a': 3}
