import math

maxNumber = 10

def is_prime(candidate: int) -> bool:
    if candidate < 2:
        return False

    for divisor in range(2, candidate):
        if(divisor <= math.sqrt(candidate)):
            if candidate % divisor == 0:
                return False
        else:
            return True

    return True

for candidate in range(1, maxNumber + 1):
    if is_prime(candidate):
        print(candidate)
