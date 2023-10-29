def flick_switch(words: list) -> list:
    result = []
    value = True
    for word in words:
        if word == 'flick':
            value = not value
        result.append(value)
    return result


print(flick_switch(['codewars', 'flick', 'code', 'wars']))
