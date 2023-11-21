def two_by_two(animals: list):
    if not animals:
        return False
    return {animal: 2 for animal in animals if animals.count(animal) >= 2}


# -> {'goat': 2, 'horse': 2}
print(two_by_two(['goat', 'goat', 'rabbit', 'rabbit', 'rabbit', 'duck', 'horse', 'horse', 'swan']))
# -> False
print(two_by_two([]))
# -> {}
print(two_by_two(['goat']))
