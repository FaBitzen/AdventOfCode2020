def same_chars(str1: str, str2: str) -> bool:
    return set(str1) == set(str2)


def same_chars2(str1: str, str2: str) -> bool:
    for i in str1:
        if i not in str2:
            return False
    for i in str2:
        if i not in str1:
            return False
    return True


print(same_chars("horse", "shoe"))
print(same_chars("horse", "shore"))
print(same_chars("twicetwice", "twice"))
print(same_chars2("horse", "shoe"))
print(same_chars2("horse", "shore"))
print(same_chars2("twicetwice", "twice"))


def invert_dict(d: dict) -> dict:
    return {val: key for key, val in d.items()}


di = {3: 5, 15: 7, 4: 64}
print(invert_dict(di))
