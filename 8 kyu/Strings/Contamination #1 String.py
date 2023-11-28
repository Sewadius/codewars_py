def contamination(text: str, char: str) -> str:
    return char * len(text) if text else ''


print(contamination('abc', 'z'))    # -> 'zzz'
print(contamination('', 'b'))       # -> ''
