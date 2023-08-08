import math

def num_paths(n):
    return math.factorial(2 * n) // (math.factorial(n)**2)


print(num_paths(1))
print(num_paths(2))
print(num_paths(10))
print(num_paths(20))
