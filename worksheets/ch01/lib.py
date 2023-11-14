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

def tournament_two(A):
    """
    Returns two largest values in A. Only works for lists whose length
    is a power of 2.
    """
    N = len(A)
    winner = [None] * (N-1)
    loser = [None] * (N-1)
    prior = [-1] * (N-1)

    # populate N/2 initial winners/losers
    idx = 0
    for i in range(0, N, 2):
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            loser[idx] = A[i]
        else:
            winner[idx] = A[i]
            loser[idx] = A[i+1]
        idx += 1

    # pair up subsequent winners and record priors
    m = 0
    while idx < N-1:
        if winner[m] < winner[m+1]:
            winner[idx] = winner[m+1]
            loser[idx]  = winner[m]
            prior[idx]  = m+1
        else:
            winner[idx] = winner[m]
            loser[idx]  = winner[m+1]
            prior[idx]  = m
        m += 2
        idx += 1

    # Find where second is hiding!
    largest = winner[m]
    second = loser[m]
    
    m = prior[m]
    while m >= 0:
        if second < loser[m]:
            second = loser[m]
        m = prior[m]
    
    return (largest, second)

def tournament_two_allow_odds(A):
    """
    Returns two largest values in A.
    """
    N = len(A)
    odd1out = 0
    if(N%2 == 1):
        odd1out = A[N - 1]
        A.pop()
        N -= 1
    
    (largest, second) = tournament_two(A)

    if(odd1out > largest):
        second = largest
        largest = odd1out
    elif(odd1out > second ):
        second = odd1out

    return (largest, second)

def two_largest_attempt(A):
    """Failed attempt to implement two largest."""
    m1 = max(A[:len(A)//2])
    m2 = max(A[len(A)//2:])
    if m1 < m2:
        return (m2, m1)
    return (m1, m2)