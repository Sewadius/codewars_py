def switch_it_up(number: int) -> str:
    numbers = ('Zero', 'One', 'Two', 'Three', 'Four',
               'Five', 'Six', 'Seven', 'Eight', 'Nine')
    return numbers[number]


print(switch_it_up(2))      # -> 'Two'
print(switch_it_up(7))      # -> 'Seven'
