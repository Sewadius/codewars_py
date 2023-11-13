def sum_str(a: str, b: str) -> str:
    if not a:
        a = 0
    if not b:
        b = 0
    return str(int(a) + int(b))


print(sum_str('', ''))      # -> '0'
print(sum_str('5', '6'))    # -> '11'
