def main(verb: str, noun: str) -> str:
    return f'{verb}{noun}'


print(main('take ', 'item'))     # -> 'take item'
print(main('use ', 'sword'))     # -> 'use sword'
