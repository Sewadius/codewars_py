def shortcut(s: str) -> str:
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''
    for ch in s:
        if ch not in vowels:
            result = f'{result}{ch}'
    return result


print(shortcut('hello'))        # -> 'hll'
print(shortcut('complain'))     # -> 'cmpln'
