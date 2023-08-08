def fib(max_val = 4_000_000):
    terms = [1, 2]
    next_val = terms[-1] + terms[-2]

    while next_val <= max_val:
        terms.append(next_val)
        next_val = terms[-1] + terms[-2]

    return terms


# Find sum of even valued terms
# Note:
#   Odd + Odd and Even + Even gives another even number
#   Sequence looks like: O, E, O, O, E, O, O, E, O, O, E, ...
#   So we want the sum of the 1st, 4th, 7th, 10th, etc

terms = fib()
print(sum(terms[1::3]))
