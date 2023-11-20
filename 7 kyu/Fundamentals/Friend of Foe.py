def friend(x: list) -> list:
    return [name for name in x if len(name) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))       # -> ['Ryan', 'Mark']
print(friend(["Jimm", "Cari", "Caret"]))         # -> ['Jimm', 'Cari']
