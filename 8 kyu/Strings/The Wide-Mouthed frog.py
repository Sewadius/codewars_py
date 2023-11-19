def mouth_size(animal: str) -> str:
    if animal.lower() == 'alligator':
        return 'small'
    return 'wide'


print(mouth_size('alligator'))      # -> 'small'
print(mouth_size('ant bear'))       # -> 'wide'
