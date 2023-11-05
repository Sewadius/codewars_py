def only_one(*args) -> bool:
    if not len(args):
        return False
    return sum(args) == 1


print(only_one())                                   # -> False
print(only_one(True, False, False))           # -> True
print(only_one(True, False, False, True))     # -> False
