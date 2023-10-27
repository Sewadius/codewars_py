def is_uppercase(inp: str) -> bool:
    return inp == inp.upper()


print(is_uppercase("c"))        # False
print(is_uppercase("HELLO"))    # True
