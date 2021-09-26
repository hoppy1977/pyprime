import math

maxNumber = 100

def is_prime(candidate: int) -> bool:
    if candidate < 2:
        return False

    divisor = 2
    while divisor <= math.sqrt(candidate):
        if candidate % divisor == 0:
            return False
        divisor += 1

    return True

for candidate in range(1, maxNumber + 1):
    if is_prime(candidate):
        print(candidate)
