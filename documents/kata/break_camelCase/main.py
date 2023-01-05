def solution(s):
    return "".join([" " + c if c in [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"] else c for c in [c for c in s]])
        
test_cases = ["helloWorld", "camelCase", "breakCamelCase"]
print([solution(test) for test in test_cases])


