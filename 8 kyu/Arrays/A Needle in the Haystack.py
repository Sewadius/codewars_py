def find_needle(haystack: list) -> str:
    position = haystack.index('needle')
    return f'found the needle at position {position}'


print(find_needle(['3', '123124234', None, 'needle', 'world']))     # -> 3
