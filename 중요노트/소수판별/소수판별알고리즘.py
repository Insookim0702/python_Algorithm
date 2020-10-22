import math

a = 16


def is_prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if i % 2 == 0:
            return False
    return True

print(is_prime(a))
