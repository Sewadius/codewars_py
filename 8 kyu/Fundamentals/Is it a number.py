def is_digit(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False


print(is_digit('s2324'))            # -> False
print(is_digit('34.65'))            # -> True
