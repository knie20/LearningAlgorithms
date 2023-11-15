from itertools import permutations
from scipy.special import factorial

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

def factorial_model(n, a):
    """Formula for A*N! with single coefficient."""
    return a*factorial(n)

def check_sorted(a):
    """Determines if list is sorted."""
    for i, val in enumerate(a):
        if i > 0 and val < a[i-1]:
            return False
    return True

def permutation_sort(A):
    """
    Generates all permutation of A until one is sorted.
    Guaranteed to sort the values in A.
    """
    for attempt in permutations(A):
        if check_sorted(attempt):
            A[:] = attempt[:]         # copy back into A
            return

def make_reversed_list(max): 
    A = list(range(0, max+1))
    return A[::-1]