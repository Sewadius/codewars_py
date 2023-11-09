def update_light(current: str) -> str:
    state = {
        'green': 'yellow',
        'yellow': 'red',
        'red': 'green'
    }
    return state.get(current)


print(update_light('green'))        # -> 'yellow'
print(update_light('yellow'))       # -> 'red'
print(update_light('red'))          # -> 'green'
