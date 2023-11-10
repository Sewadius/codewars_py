def bonus_time(salary: int, bonus: bool) -> str:
    return f'${salary * 10}' if bonus else f'${salary}'


print(bonus_time(10000, True))      # -> $100000
print(bonus_time(60000, False))     # -> $60000
