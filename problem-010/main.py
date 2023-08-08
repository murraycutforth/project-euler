import math

N = 2_000_000
primes = [False, False] + [True] * (N - 1)

# Implement seive of eratosthenes
for i in range(2, int(math.sqrt(N)) + 1):
    if primes[i]:
        k = 2 * i

        # Remove all multiples of i
        while k <= N:
            primes[k] = False
            k += i

result = 0
for i in range(len(primes)):
    result += i * int(primes[i])

print(result)


