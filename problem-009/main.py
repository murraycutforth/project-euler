import sys

# a < b < c
# a + b + c = 1000
# So a < b < 1000 - a - b
# And a must lie in [1, 332], b must lie in [2, 499], c must lie in [334, 997]

for a in range(1, 333):
    b = a + 1
    while b < 1000 - a - b:
        c = 1000 - a - b

        if a**2 + b**2 == c**2:
            print(a, b, c)
            print(a * b * c)
            sys.exit()

        b += 1
            

# (a + b + c)^2 = 1,000,000
# a^2 + b^2 + c^2 + 2ab + 2ac + 2bc = 1,000,000
# 2c^2 + 2(ab + ac + bc) = 1,000,000

