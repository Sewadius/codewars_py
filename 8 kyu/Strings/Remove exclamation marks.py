def remove_exclamation_marks(s: str) -> str:
    result = ''
    for ch in s:
        if ch != '!':
            result = f'{result}{ch}'
    return result


print(remove_exclamation_marks('Hello World!!!'))       # -> 'Hello World'
print(remove_exclamation_marks('Hi! Hello!'))           # -> 'Hi Hello'
