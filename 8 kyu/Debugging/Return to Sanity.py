def mystery() -> dict:
    return {'sanity': 'Hello'}


print(type(mystery()))          # -> <class 'dict'>
print(mystery()['sanity'])      # -> 'Hello'
