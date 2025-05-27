from itertools import chain, combinations

def power(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s) + 1)))

set = [1, 2, 3]
print('Power Set :', power(set))