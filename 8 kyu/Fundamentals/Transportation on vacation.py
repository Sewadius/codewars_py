def rental_car_cost(d: int) -> int:
    total = d * 40
    if d > 6:
        total -= 50
    elif d > 2:
        total -= 20
    return total


print(rental_car_cost(1))       # -> 40
print(rental_car_cost(4))       # -> 140
print(rental_car_cost(7))       # -> 230
