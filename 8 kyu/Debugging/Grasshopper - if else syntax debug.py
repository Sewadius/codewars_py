def check_alive(health: int) -> bool:
    return health > 0


print(check_alive(5))       # -> True
print(check_alive(0))       # -> False
