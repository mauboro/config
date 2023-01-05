def bouncing_ball(arr):
    h, b, w = arr
    if h > 0 and b > 0 and b < 1 and w < h:
        count = 1 
        current = h * b
        while current > w:
            count += 2
            current *= b
        return count
    else:
        return -1

test_cases = [(2, 0.5, 1), (3, 0.66, 1.5), (30, 0.66, 1.5), (30, 0.75, 1.5)]
print([bouncing_ball(test) for test in test_cases])

