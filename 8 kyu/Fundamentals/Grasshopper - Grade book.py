def get_grade(s1: int, s2: int, s3: int) -> str:
    score = (s1 + s2 + s3) / 3
    if 100 >= score >= 90:
        return 'A'
    if 90 > score >= 80:
        return 'B'
    if 80 > score >= 70:
        return 'C'
    return 'D' if 70 > score >= 60 else 'F'


print(get_grade(95, 90, 93))        # -> 'A'
print(get_grade(70, 70, 70))        # -> 'C'
