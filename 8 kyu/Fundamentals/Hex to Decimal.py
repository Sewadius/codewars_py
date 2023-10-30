def hex_to_dec(s: str) -> int:
    return int(s, 16)


print(hex_to_dec('a'))      # -> 10
print(hex_to_dec('ff'))     # -> 255
