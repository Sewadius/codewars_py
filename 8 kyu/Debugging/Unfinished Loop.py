def create_array(n: int) -> list:
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


print(create_array(2))      # -> [1, 2]
print(create_array(4))      # -> [1, 2, 3, 4]
