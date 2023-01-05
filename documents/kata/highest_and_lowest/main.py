def high_and_low(numbers):
    n_list = [int(n) for n in numbers.split(" ") ]
    return f"{max(n_list)} {min(n_list)}"
