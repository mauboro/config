def enough(cap, on, wait):
    return 0 if (on + wait - cap) < 0 else (on + wait - cap)

def enough_refactored(cap, on, wait):
    return max(0, on + wait - cap)
