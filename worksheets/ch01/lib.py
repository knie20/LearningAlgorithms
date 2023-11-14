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

def counting_sort_improved(A, M):
    counts = [0] * (M + 1)
    for v in A:
        counts[v] += 1

    pos = 0
    v = 0
    while pos < len(A):
        cnt = counts[v]
        A[pos:pos+cnt] = [v] * cnt
        pos += cnt
        v += 1