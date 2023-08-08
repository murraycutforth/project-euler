
def manual_multiply(num: list, factor: int):
    rem = 0
    for i in range(len(num)):
        x = num[i] * factor + rem
        num[i] = x % 10
        rem = x // 10

    if rem > 0:
        num.append(rem)

    return num


def power(base, exponent):
    num = [1]
    for i in range(exponent):
        num = manual_multiply(num, base)
    return num


def listsum(arr):
    s = 0
    for x in arr:
        s += x
    return s


base = 2
exponent = 1000
result = listsum(power(base, exponent))

print(result)
        




