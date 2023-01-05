import string

def high(x):
    # Code here
    dicto = {l: i + 1 for i, l in enumerate(string.ascii_lowercase)}
    words_score = {}
    for w in x.split(" "):
        words_score.update({w: (sum(dicto[l] for l in w), x.split(" ").index(w) )})

    high_word = "".join([key for key, value in words_score.items() if value == max(words_score.values())])
    smallest_index = words_score[high_word][1]
    for key, value in words_score.items():
        if key == high_word:
            if value[1] < smallest_index:
                smallest_index = value[1]
                high_word = key

    print(high_word)
    

test_cases = ['man i need a taxi up to ubud', 'what time are we climbing up the volcano', 'take me to semynak', 'aa b', 'b aa', 'bb d', 'd bb', "aaa b"]

print([high(test) for test in test_cases])
print("taxi", "volcano", "semynak", "aa", "b", "bb", "d", "aaa")
