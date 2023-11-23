def replace_dots(s: str) -> str:
    return s.replace('.', '-')


print(replace_dots('.....'))        # -> '-----'
print(replace_dots('no dots'))      # -> 'no dots'
