def xo(s: str) -> bool:
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo('zpzpzpp'))    # -> True
print(xo('ooxXm'))      # -> True
