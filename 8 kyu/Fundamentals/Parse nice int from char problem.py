def get_age(age: str) -> int:
    return int(age.split()[0])


print(get_age('2 years old'))       # -> 2
print(get_age('11 years old'))      # -> 11