
import random, copy
from algs.counting import RecordedItem
from algs.table import DataTable
from ch01.challenge import linear_median

# A = list([RecordedItem(i) for i in range(n)])
# random.shuffle(A)

table = DataTable([8,15,15],
                    ['N', 'linear_median', 'sorted_median'])

def sorted_median(A):
    return sorted(A)[len(A)//2]


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

