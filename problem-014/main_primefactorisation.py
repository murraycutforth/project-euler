from collections import defaultdict
import math
from functools import lru_cache


@lru_cache(maxsize=1_000_000)
def is_prime(x):
    if x == 2 or x == 3:
        return True
    #if (x + 1) % 6 != 0 and (x - 1) % 6 != 0:
    #    return False
    if x % 2 == 0:
        return False
    for i in range(3, x // 2 + 1, 2):
        if x % i == 0:
            return False
    return True


@lru_cache(maxsize=1_000_000)
def prime_factors(x):
    # Return [prime factors], [exponents]
    # Any number can only have 1 prime factor greater than sqrt(x)
    factors = defaultdict(int)
    while x > 1:
        if is_prime(x):
            factors[x] += 1
            return factors
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0 and is_prime(i):
                factors[i] += 1
                x = x // i
                break
    return factors



def jump_next_val(n):
    if n % 2 == 0:
        factors = prime_factors(n)
        return factors[2], n // 2**factors[2]
    else:
        return 1, 3 * n + 1


def collatz_sequence_length(n):
    length = 1
    while n != 1:
        steps, n = jump_next_val(n)
        length += steps
    return length


longest = (None, 0)
for i in range(1, 1_000):
    seq_len = collatz_sequence_length(i)
    print(i, seq_len)
    if seq_len > longest[1]:
        longest = (i, seq_len)

print(longest)
