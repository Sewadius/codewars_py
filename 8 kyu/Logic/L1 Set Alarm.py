def set_alarm(employed: bool, vacation: bool) -> bool:
    return employed and not vacation


print(set_alarm(True, False))       # -> True
print(set_alarm(True, True))        # -> False
print(set_alarm(False, False))      # -> False
