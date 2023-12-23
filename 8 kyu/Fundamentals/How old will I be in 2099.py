def calculate_age(birth: int, current: int) -> str:
    if birth - 1 == current:
        return f'You will be born in 1 year.'
    elif current - 1 == birth:
        return 'You are 1 year old.'
    elif birth == current:
        return 'You were born this very year!'
    elif birth > current:
        return f'You will be born in {birth - current} years.'
    else:
        return f'You are {current - birth} years old.'
