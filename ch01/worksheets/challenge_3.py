import random
from algs.table import DataTable


def counting_sort(A, M):
    """
    Update A in place to be sorted in ascending order if all elements
    are guaranteed to be in the range 0 to and not including M.
    """
    counts = [0] * (M + 1)
    for v in A:
        counts[v] += 1

    pos = 0
    v = 0
    while pos < len(A):
        for idx in range(counts[v]):
            A[pos+idx] = v
        pos += counts[v]
        v += 1

def use_counting_sort():
    table = DataTable([8, 15], ['N', 'time'])
    trials = [2**k+1 for k in range(1, 15)]
    M = 20

    for n in trials:
        A = [random.randint(0, M) for _ in range(n)]
        random.shuffle(A)
        counting_sort(A, M)

use_counting_sort()