def count_sheep(n: int) -> str:
    result = ''
    for i in range(1, n + 1):
        result = f'{result}{i} sheep...'
    return result


print(count_sheep(0))       # -> ''
print(count_sheep(2))       # -> '1 sheep...2 sheep...'
