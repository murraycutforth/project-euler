# Find sum of even valued terms
# Note:
#   Odd + Odd and Even + Even gives another even number
#   Sequence looks like: O, E, O, O, E, O, O, E, O, O, E, ...
#   So we want the sum of the 1st, 4th, 7th, 10th, etc

# We also don't need to store the entire array, just compute on the fly and then discard
# So we can write a function to skip from one even term to the next

method = 2

if method == 1:

    def next_pair(x_0, x_1):
        x_n2 = 2 * x_1 + x_0
        x_n3 = 2 * x_0 + 3 * x_1
        return x_n2, x_n3
    
    result = 0
    
    pair = (1, 2)
    
    while(pair[1] < 4_000_000):
        result += pair[1]
        pair = next_pair(*pair)
    
    print(result)


# This can be improved on by finding the recurrence relation F(n) = 4 F(n-3) + F(n-6)

if method == 2:
    
    def next_even_term(x_0, x_1):
        return 4 * x_1 + x_0
    
    x_0 = 2
    x_1 = 8
    temp = 0
    result = x_0
    
    while x_1 <= 4_000_000:
        result += x_1
        temp = x_1
        x_1 = next_even_term(x_0, x_1)
        x_0 = x_1
    
    print(result)

