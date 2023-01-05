def solution(t, e):
    return e in t if e[-1] == t[-1] else False

def solution_refactored(t, e):
    return t.endswith(e)

def another_solution(t, e):
    return e in t[-(len(e)):]
