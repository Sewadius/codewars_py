def hello(name: str = '') -> str:
    if name == '':
        return 'Hello, World!'
    return f'Hello, {name.capitalize()}!'


print(hello('aliCE'))  # -> 'Hello, Alice!'
print(hello())  # -> 'Hello, World!'
