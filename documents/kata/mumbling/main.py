def accum(s):
    result = []
    for i, l in enumerate(s):
        result.append(f"{l.upper()}{(l * i).lower()}")
        result.append("-")
    return "".join(result)[:-1]

def accum_refactored(s):
    return "-".join(c.upper() + c.lower() * i for i, c in enumerate(s, start=1))
