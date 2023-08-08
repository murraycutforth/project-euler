import math


def is_prime(x):
    # Correct for x >= 1
    # Any number x can only have 1 prime factor greater than sqrt(x)
    # Therefore if there are no factors <= sqrt(x) then x itself must be prime
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = 2
x = 3

while n < 10_001:
    x += 2
    if is_prime(x):
        n += 1
        print(f"{n:06}", end="\r")

print(x)
