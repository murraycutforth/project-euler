
def divisible(x, N):
    for i in range(1, N):
        if x % i != 0:
            return False
    return True

N = 20
result = N

while not divisible(result, N):
    result += N

print(result)

