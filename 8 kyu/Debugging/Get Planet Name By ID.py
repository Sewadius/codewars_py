def get_planet_name(num: int) -> str:
    planets = (
        'Mercury',
        'Venus',
        'Earth',
        'Mars',
        'Jupiter',
        'Saturn',
        'Uranus',
        'Neptune'
    )
    return planets[num - 1]


print(get_planet_name(2))       # Venus
