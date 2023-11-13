import random, copy, timeit
from algs.counting import RecordedItem
from algs.table import DataTable
from ch01.challenge import linear_median
from ch01.challenge import counting_sort
from algs.sorting import is_sorted

# A = list([RecordedItem(i) for i in range(n)])
# random.shuffle(A)



def sorted_median(A):
    return sorted(A)[len(A)//2]


def liner_median_trials(sorted_median):
    table = DataTable([8,15,15],
                    ['N', 'linear_median', 'sorted_median'])
    trials = [2**k+1 for k in range(1, 15)]
    for n in trials:
        A = list([RecordedItem(i) for i in range(n)])
        random.shuffle(A)
        B = copy.deepcopy(A)

        RecordedItem.clear()
        med1 = linear_median(A)
        result1 = RecordedItem.report()[1]

    
        RecordedItem.clear()
        med2 = sorted_median(B)
        result2 = RecordedItem.report()[1]

        assert med1 == med2

        table.row([n, result1, result2])


# example on how to use timeit
def timeit_demo():
    M = 10
    n = 0
    setup = '''
    import random
    from ch01.challenge import counting_sort
    from algs.sorting import is_sorted
    w = [{0}-1] * {1}
    b = [0] * {1} 
    a = list(range({0})) * {1}
    random.shuffle(a)
    '''.format(M,n)
    print(timeit.repeat(stmt='This is what we are timing', setup=setup, repeat=100, number=1))

def time_counting_sort():
    table = DataTable([8, 15], ['N', 'time'])
    trials = [2**k+1 for k in range(1, 15)]
    setup = '''
import random
from ch01.challenge import counting_sort
from algs.sorting import is_sorted
a = list(range({0})) * {1}
random.shuffle(a)
'''
    stmt = '''
counting_sort(a,{})
is_sorted(a)
'''

    M = 30
    for n in trials:
        cs_time = min(timeit.repeat(stmt=stmt.format(n), setup=setup.format(M, n), repeat=100, number=1))
        table.row([n, cs_time])

# time_counting_sort()

def use_counting_sort():
    table = DataTable([8, 15], ['N', 'time'])
    trials = [2**k+1 for k in range(1, 15)]
    M = 20

    for n in trials:
        A = [random.randint(0, M) for _ in range(n)]
        random.shuffle(A)
        counting_sort(A, M)

use_counting_sort()