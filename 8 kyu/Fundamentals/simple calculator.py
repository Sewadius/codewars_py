def calculator(x: int, y: int, op: str):
    if (
        op in {'+', '-', '*', '/'}
        and isinstance(x, int)
        and isinstance(y, int)
    ):
        return eval(f'{x}{op}{y}')
    return 'unknown value'


print(calculator(1, 2, '+'))    # -> 3
print(calculator(1, 2, '^'))    # -> 'unknown value'
print(calculator(6, '$', '+'))  # -> 'unknown value'
