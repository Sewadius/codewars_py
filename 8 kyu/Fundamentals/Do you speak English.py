def sp_eng(sentence: str) -> bool:
    return 'english' in sentence.lower()


print(sp_eng('1234english ;k'))     # -> True
print(sp_eng('egnlish'))            # -> False
