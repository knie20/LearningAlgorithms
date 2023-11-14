import random
import timeit
from algs.sorting import is_sorted
from algs.table import DataTable

MAX_NUM = 20
table = DataTable([8, 15, 15, 15], ['N', 'cs_min', 'csi_min', 'improvement%'])
trials = [2**k for k in range(1, 18)]
exec_cs = '''
counting_sort(A, M)
is_sorted(A)'''
setup_cs = '''
import random
from worksheets.ch01.lib import counting_sort
from algs.sorting import is_sorted
M = {0}
n = {1}
A = [random.randint(0, M) for _ in range(n)]
random.shuffle(A)'''

exec_csi = '''
counting_sort_improved(A, M)
is_sorted(A)'''
setup_csi = '''
import random
from worksheets.ch01.lib import counting_sort_improved
from algs.sorting import is_sorted
M = {0}
n = {1}
A = [random.randint(0, M) for _ in range(n)]
random.shuffle(A)'''

for n in trials:
    cs_time = min(timeit.repeat(exec_cs, setup_cs.format(MAX_NUM, n), repeat=20, number=1))
    csi_time = min(timeit.repeat(exec_csi, setup_csi.format(MAX_NUM, n), repeat=5, number=1))
    table.row([n, cs_time * 1000, csi_time * 1000, (cs_time - csi_time) * 100 / cs_time])
