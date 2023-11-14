import random

from worksheets.ch01.lib import tournament_two


trials = [2**k-2 for k in range(2, 9)]

for n in trials:
    A = list(range(1, n))
    random.shuffle(A)
    B = [*A, n]

    print('length: ', len(B))

    (one, two) = tournament_two(B)

    assert(one == n)
    assert(two == n-1)
    print(one, two)