def final_grade(exam: int, projects: int) -> int:
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and projects > 4:
        return 90
    if exam > 50 and projects > 1:
        return 75
    return 0


print(final_grade(100, 12))     # -> 100
print(final_grade(85, 5))       # -> 90
print(final_grade(55, 3))       # -> 75
print(final_grade(55, 0))       # -> 0
