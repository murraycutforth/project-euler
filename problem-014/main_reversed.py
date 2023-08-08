import queue


#class Tree:
#    def __init__(self, val, depth):
#        self.val = val
#        self.depth = depth
#        self.children = []
#    def __repr__(self):
#        return f"{self.val}"


def next_vals(n):
    if (n-1) % 3 == 0 and n > 4 and ((n-1) // 3) % 2 == 1:
        return [(n-1) // 3, n * 2]
    else:
        return [n * 2]


#root = Tree(1, 1)

nq = queue.Queue() # Use FIFO to build tree breadth-first (LIFO = depth first)
nq.put((1, 1))
longest_chain = (None, 1)
n = 1

while not nq.empty():
    current_val, current_depth = nq.get()

    if current_depth > 200:
        break

    nv = next_vals(current_val)

    for val in nv:
        if val > 100_000_000:
            continue

        n += 1

        depth = current_depth + 1

        nq.put((val, depth))

        if val < 1_000_000 and depth > longest_chain[1]:
            longest_chain = (val, depth)

print(n)
print(longest_chain)








