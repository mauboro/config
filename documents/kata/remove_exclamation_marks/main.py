def remove_exclamation_marks(s):
    return "".join(s.split("!"))

def remove_exclamation_marks_refactored(s):
    return s.replace("!", "")
