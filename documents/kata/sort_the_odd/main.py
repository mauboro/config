def sort_array(source_array):
    odd_list = []
    result = []
    count = 0
    odd_list = [n for n in source_array if n % 2 != 0]
    odd_list.sort()
    for n in source_array:
        if n % 2 != 0:
            result.append(odd_list[0 + count])
            count += 1
        elif n % 2 == 0:
            result.append(n)

    print(result)

test_cases = [[5, 3, 2, 8, 1, 4], [5, 3, 1, 8, 0]]
[sort_array(test) for test in test_cases]

def sort_array_refactored(arr):
    odds_list = sorted((n for n in arr if n % 2 != 0 ), reverse=True)
    return [n if n % 2 == 0 else odds_list.pop() for n in arr]
    
[print(sort_array_refactored(test)) for test in test_cases]


