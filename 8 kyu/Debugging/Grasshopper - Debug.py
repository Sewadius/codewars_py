def weather_info(temp: int) -> str:
    c = convert_to_celsius(temp)
    if c > 0:
        return f'{c} is above freezing temperature'
    return f'{c} is freezing temperature'


def convert_to_celsius(temperature: int) -> float:
    return (temperature - 32) * (5 / 9)


print(weather_info(50))     # '10.0 is freezing temperature'
print(weather_info(23))     # '-5.0 is freezing temperature'
