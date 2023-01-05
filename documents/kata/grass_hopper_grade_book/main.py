
def get_grade(grade_tuple):
    s1, s2, s3 = grade_tuple
    average = (s1 + s2 + s3) / 3
    if  90 <= m <= 100:
        return "A"
    elif  80 <= m <= 90:
        return "B"
    elif  70 <= m <= 80:
        return "C"
    elif 60 <= m < 70
        return "D"
    else:
        return "F"


test_cases = [(95, 90, 93), (100, 85, 96), (92, 93, 94)]
print([get_grade(test) for test in test_cases])

