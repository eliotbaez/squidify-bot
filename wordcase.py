LOWERCASE = 0
UPPERCASE = 1
CAPITAL_FIRST = 2
LOWER_FIRST = 3


def get_case(word: str) -> int:
    if word.islower():
        return LOWERCASE
    if word.isupper():
        return UPPERCASE
    # it must be mixed then. What kind of mixed?
    if word[:1].isupper():
        return CAPITAL_FIRST
    return LOWER_FIRST


def set_case(word: str, wordcase: int) -> str:
    if wordcase == LOWERCASE:
        return word.lower()
    if wordcase == UPPERCASE:
        return word.upper()
    if wordcase == CAPITAL_FIRST:
        r = word.lower()
        r = r[0].upper() + r[1:]
        return r
    if wordcase == LOWER_FIRST:
        r = word.upper()
        r = r[0].lower() + r[1:]
        return r

