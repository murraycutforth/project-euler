# The N-th triangle number is given by \SUM_{i=1}^{N} i = 0.5 * i * (i + 1). Alternatively, there is a recurrence relation of N_{i} = N_{i-1} + i.
# We want to find the first triangle number with over K divisors.

import math

K = 500


def num_divisors(n):
    num_div = 0
    for i in range(1, n // 2):
        if n % i == 0:
            num_div += 1
    num_div *= 2
    print(n, num_div)
    return num_div


def triangle_gen_expr():
    i = 1
    tri_num = 1

    while True:
        yield tri_num
        i += 1
        tri_num += i


# This naive search approach takes far too long. Checking the number of divisors is O(N). And the i-th triangle number is O(i^2).
# This means that the effort required to check the number of divisors increases quadratically as we proceed along the sequence.

#for k in triangle_gen_expr():
#    num_div = num_divisors(k)
#    if num_div >= K:
#        break


# Instead, how can we reduce the effort of checking the number of divisors of a number?
# If i = 0.5 * n * (n + 1), does this tell us about the number of divisors?
# For example, if n = 10 -> 1*10, 2*5, n + 1 = 11 -> 1*11, then 55 = 0.5 * 1*10*1*11, or 0.5*2*5*1*11 -> 1*55, 5*11
# As another example, if n=8 -> 1*8, 2*4, if n=9 -> 1*9, 3*3, then 36 = 0.5 * 1*8*1*9 = 0.5 * 1*8*3*3 = 0.5 * 2*4*1*9 = 0.5 * 2*4*3*3 -> 1*36, 2*18, 3*12, 4*9, 6*6

# Let's try another approach based on prime factors
# If k has x prime factors, then the total number of factors is 2 + 2^(x-1)
# Now we just need to find the number of prime factors of k
# Can we compute prime factors recursively?
# If {x_1, x_2, x_3, ...} are the set of prime factors for k, what are the prime factors of k+a?
# k+a = (x_1*x_2*x_3*...) + (a_1*a_2*...) where a_i are the prime factors of a
# k+a = (c_1*c_2*...)(y_1*y_2*... + b_1*b_2*...) where c_i are the common prime factors
# So we can just find prime factors of y_1*y_2+... + b_1*b_2*...

# After some testing, I've realised this isn't true. If k=a*b*c, where a,b,c are prime, then we can write k in terms of 2^(3-1) different splits:
    # {a, bc}, {ab, c}, {b, ac}, {, abc}. We want to count number of distinct elements in {a, b, c, ab, ac, bc, abc} to get number of factors (not including 1).


from functools import lru_cache

@lru_cache(maxsize=1_000_000)
def is_prime(x):
    # Correct for x >= 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def prime_factors(n):
    # Note: excluding n itself, so will return [] for primes
    factors = []
    while n > 1:
        if is_prime(n):
            factors.append(n)
            break
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
                n //= i
                break
    return factors


from itertools import chain, combinations


def powerset(iterable):
    return chain.from_iterable(combinations(iterable, r) for r in range(len(iterable) + 1))

def product(iterable):
    result = 1
    for k in iterable:
        result *= k
    return result


for k in triangle_gen_expr():
    p_factors = prime_factors(k)
    factors = set(product(p) for p in powerset(p_factors))
    print(p_factors, factors)
    num_div = len(factors)
    print(k, num_div)
    print()
    if num_div >= K:
        break

print(k)


# This isfar more efficient because 

