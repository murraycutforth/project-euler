def next_val(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def collatz_sequence(n):
    yield n
    while n != 1:
        n = next_val(n)
        yield n


longest = (None, 0)
for i in range(1, 1_000_000):
    seq_len = len(list(collatz_sequence(i)))
    if seq_len > longest[1]:
        longest = (i, seq_len)

print(longest)
