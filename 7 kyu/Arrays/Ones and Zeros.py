def binary_array_to_number(arr: list) -> int:
    number_str = ''
    for number in arr:
        number_str = f'{number_str}{number}'
    return int(number_str, 2)


print(binary_array_to_number([1,1,1,1]))        # -> 15
print(binary_array_to_number([0,1,1,0]))        # -> 6
