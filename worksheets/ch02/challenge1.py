def fragment_1(N):
    """O(N)"""
    ct = 0
    for _ in range(100):
        for _ in range(N):
            for _ in range(10000):
                ct += 1
    return ct

def fragment_2(N):
    """O(N^2)"""
    ct = 0
    for _ in range(N):
        for _ in range(N):
            for _ in range(100):
                ct += 1
    return ct

def fragment_3(N):
    """O(N^2)"""
    ct = 0
    for _ in range(0,N,2):
        for _ in range(0,N,2):
            ct += 1
    return ct

def fragment_4(N):
    """O(log(N))"""
    ct = 0
    while N > 1:
        ct += 1
        N = N // 2
    return ct

def fragment_5(N):
    """O(N^2)"""
    ct = 0
    for _ in range(2,N,3):
        for _ in range(3,N,2):
            ct += 1
    return ct

