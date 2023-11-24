def converter(mpg: int) -> float:
    return round(mpg / 4.54609188 * 1.609344, 2)


print(converter(12))        # -> 4.25
print(converter(36))        # -> 12.74
