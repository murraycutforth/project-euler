N = 1000
s = 0

for i in range(N):
    if i % 3 == 0 or i % 5 == 0:
        s += i

print(s)
