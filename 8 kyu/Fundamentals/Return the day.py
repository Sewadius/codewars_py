def whatday(num: int) -> str:
    error = 'Wrong, please enter a number between 1 and 7'
    days = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday')
    return days[num - 1] if 0 < num < 8 else error


print(whatday(3))       # -> 'Tuesday'
print(whatday(1))       # -> 'Sunday'
