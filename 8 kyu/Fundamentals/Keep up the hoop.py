def hoop_count(n: int) -> str:
    if n > 9:
        return 'Great, now move on to tricks'
    return 'Keep at it until you get it'


print(hoop_count(3))        # -> 'Keep at it until you get it'
print(hoop_count(11))       # -> 'Great, now move on to tricks'
