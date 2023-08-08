def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = 2 ** 1000
digit_sum = sum_of_digits(number)

print("The sum of the digits of 2^1000 is:", digit_sum)

