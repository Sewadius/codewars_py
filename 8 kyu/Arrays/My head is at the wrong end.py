def fix_the_meerkat(arr: list) -> list:
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


print(fix_the_meerkat(['tail', 'body', 'head']))        # -> ['head', 'body', 'tail']
print(fix_the_meerkat(['ground', 'rainbow', 'sky']))    # -> ['sky', 'rainbow', 'ground']
