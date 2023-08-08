def is_pal(x):
    x_str = str(x)
    return x_str == x_str[::-1]

largest_pal = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        if is_pal(i * j):
            largest_pal = max(largest_pal, i * j)

print(largest_pal)

