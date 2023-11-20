def to_jaden_case(string: str) -> str:
    return ' '.join(map(str.capitalize, string.split()))


# -> "How Can Mirrors Be Real If Our Eyes Aren't Real"
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
