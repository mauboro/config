def count_positives_sum_negatives(arr):
    return [sum(1 for n in arr if n > 0), sum(n for n in arr if n < 0)] if arr else []
