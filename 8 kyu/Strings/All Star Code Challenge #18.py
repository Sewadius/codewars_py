def str_count(strng: str, letter: str) -> int:
    return strng.count(letter)


print(str_count('Hello', 'l'))      # -> 2
print(str_count('ggggg', 'g'))      # -> 5
