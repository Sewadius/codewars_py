def problem(a):
    if isinstance(a, str):
        return 'Error'
    return a * 50 + 6


print(problem('hello'))     # -> 'Error'
print(problem(1))           # -> 56
