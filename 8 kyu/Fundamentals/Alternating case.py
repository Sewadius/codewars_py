def to_alternating_case(string: str) -> str:
    result = ''
    for ch in string:
        if ch.islower():
            result = f'{result}{ch.upper()}'
        else:
            result = f'{result}{ch.lower()}'
    return result


print(to_alternating_case('hello world'))       # -> 'HELLO WORLD'
print(to_alternating_case('12345'))             # -> '12345'
