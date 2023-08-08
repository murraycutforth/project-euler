from functools import lru_cache

@lru_cache(maxsize=1_000_000)
def is_prime(x):
    # Correct for x >= 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def find_factors(x, factors):
    print(x, factors)
    if is_prime(x):
        factors.append(x)
        return
    else:
        for i in range(2, x // 2):
            if x % i == 0 and is_prime(i):
                factors.append(i)
                find_factors(x // i, factors)
                break


factors = []
find_factors(600851475143, factors)
print()
print(max(factors))
