from math import sqrt

def is_prime(n):
    if n <= 1:
        return False

    for i in range(sqrt(n) + 1):
        if n % i == 0:
            return False

    return True
