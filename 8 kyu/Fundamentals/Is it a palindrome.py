def is_palindrome(s: str) -> bool:
    return s.lower() == s.lower()[::-1]


print(is_palindrome('Abba'))        # -> True
print(is_palindrome('walter'))      # -> False
