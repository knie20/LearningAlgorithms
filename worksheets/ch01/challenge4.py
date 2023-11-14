import random

from worksheets.ch01.lib import tournament_two, tournament_two_allow_odds

def run_tournament_two_trials(max_k=15):
    trials = [(2**k) for k in range(2, max_k)]
    for n in trials:
        A = list(range(1, n))
        random.shuffle(A)
        B = [*A, n]

        print('length: ', len(B))

        (one, two) = tournament_two(B)

        assert(one == n)
        assert(two == n-1)
        print(one, two)

def run_tournament_two_allow_odds_trials(max_k=15):
    trials = [(2**k)-1 for k in range(2, max_k)]
    for n in trials:
        A = list(range(1, n))
        random.shuffle(A)
        B = [*A, n]

        print('length: ', len(B))

        (one, two) = tournament_two_allow_odds(B)

        assert(one == n)
        assert(two == n-1)
        print(one, two)

run_tournament_two_allow_odds_trials()