def is_leap_year(year: int) -> bool:
    return bool(not year % 4 and (year % 100 or not year % 400))


print(is_leap_year(2015))       # -> False
print(is_leap_year(2020))       # -> True
print(is_leap_year(2000))       # -> True
print(is_leap_year(2100))       # -> False
