def duplicate_encode(word: str) -> str:
    return ''.join(')' if word.lower().count(ch) > 1 else '(' for ch in word.lower())


print(duplicate_encode('din'))      # -> '((('
print(duplicate_encode('Success'))  # -> ')())())'
