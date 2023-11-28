def type_validation(variable, _type: str) -> bool:
    return _type in str(type(variable))


print(type_validation(42, 'int'))       # -> True
print(type_validation('42', 'int'))     # -> False
