def collatz_sequence_len(n, precomputed_terms):
    if n in precomputed_terms:
        return precomputed_terms[n]

    if n % 2 == 0:
        precomputed_terms[n] = 1 + collatz_sequence_len(n // 2, precomputed_terms)
    else:
        precomputed_terms[n] = 1 + collatz_sequence_len(3 * n + 1, precomputed_terms)

    return precomputed_terms[n]



precomputed_terms = {1: 1}
longest = (None, 0)

for i in range(1, 1_000_000):
    seq_len = collatz_sequence_len(i, precomputed_terms)

    if seq_len > longest[1]:
        longest = (i, seq_len)

print(longest)
