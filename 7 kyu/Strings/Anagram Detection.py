def is_anagram(test: str, original: str) -> bool:
    return set(test.lower()) == set(original.lower()) and len(test) == len(original)


print(is_anagram('foefet', 'toffee'))           # -> True
print(is_anagram('Buckethead', 'DeathCubeK'))   # -> True
print(is_anagram('apple', 'pale'))              # -> False
