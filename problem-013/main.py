with open("numbers.txt") as infile:
    text = infile.readlines()

# We want to find the first 10 digits of the sum
# There are 100 numbers - how many places can affect the first 10 digits of the sum?
# Just the first 12 places need to be summed - from beyond the cannot influence the 10th digit
# Sum the numbers in the i-th column, and then multiply by 10**(10 - i)

result = 0
for i in range(12):
    for num_str in text:
        result += int(num_str[i]) * 10**(11 - i)
print(result)

import math
n_digits = math.floor(math.log10(result) + 1)
print(result // (10**(n_digits - 10)))

