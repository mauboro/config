def printer_error(s):
    errors = 0
    letters = "abcdefghijklm"
    for l in s:
        if l not in letters:
            errors +=1
    
    return f"{errors}/{len(s)}"
