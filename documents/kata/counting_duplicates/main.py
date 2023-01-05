def duplicate_count(text):
    total = 0
    repeated_letters = []
    text_list = ([c for c in text.lower()])
    for c in text_list:
        if text_list.count(c) > 1 and c not in repeated_letters:
            repeated_letters.append(c)
            total += 1 

    print(total)




test_cases = ["abcde", "abcdeaa", "abcedaB", "Indivisibilities"]
[duplicate_count(test) for test in test_cases]
