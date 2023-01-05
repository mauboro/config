def is_palindrome(s):
    my_list = [c for c in s]
    my_list.reverse()
    my_string = "".join(my_list)
    if my_string.upper() == s.upper():
        return True
    else:
        return False

print(is_palindrome("helloworld"))
print(is_palindrome("kodok"))

def is_palindrome_refactored(s):
    return s.lower() == s.lower()[::-1]

print(is_palindrome_refactored("helloworld"))
print(is_palindrome_refactored("kodok"))

