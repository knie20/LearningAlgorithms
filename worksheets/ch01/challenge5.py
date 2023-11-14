import random

from worksheets.ch01.lib import two_largest_attempt


def trials_that_fail(max_k = 15):
    trials = [2**k for k in range(3, max_k)]
    for n in trials:
        A = list(range(1, n+1))
        random.shuffle(A)
        N = len(A)
        random_number_1 = random.randint(0, N//2)
        random_number_2 = random.randint(0, N//2)

        while random_number_1 == random_number_2:
            random_number_2 = random.randint(0, N//2)
        
        A[random_number_1] = n+1
        A[random_number_2] = n+2

        (one, two) = two_largest_attempt(A)

        assert(one == n+2)
        assert(two != n+1)
    
trials_that_fail()
