def fragment_1(N):
    """Fragment-1 for exercise."""
    ct = 0
    for _ in range(100):
        for _ in range(N):
            for _ in range(10000):
                ct += 1
    return ct

def fragment_2(N):
    """Fragment-2 for exercise."""
    ct = 0
    for _ in range(N):
        for _ in range(N):
            for _ in range(100):
                ct += 1
    return ct

def fragment_3(N):
    """Fragment-3 for exercise."""
    ct = 0
    for _ in range(0,N,2):
        for _ in range(0,N,2):
            ct += 1
    return ct

def fragment_4(N):
    """Fragment-4 for exercise."""
    ct = 0
    while N > 1:
        ct += 1
        N = N // 2
    return ct

def fragment_5(N):
    """Fragment-5 for exercise."""
    ct = 0
    for _ in range(2,N,3):
        for _ in range(3,N,2):
            ct += 1
    return ct

def f4(N):
    """Fragment for exercise."""
    ct = 1
    while N >= 2:
        ct = ct + 1
        N = N ** 0.5
    return ct