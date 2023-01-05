import string

def same_case(a, b):
    return -1 if a not in string.ascii_letters or b not in string.ascii_letters else 1 if a in string.ascii_uppercase and b in string.uppercase or a in string.ascii_lowercase or b in string.ascii_lowercase else 0 

def same_case_refactored(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha else -1

