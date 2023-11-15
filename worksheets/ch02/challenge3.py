import timeit
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from algs.table import DataTable
from worksheets.ch02.lib import f4, factorial_model, make_reversed_list, permutation_sort

model = factorial_model
algo = permutation_sort


N = [k for k in range(2, 12)]
X = [make_reversed_list(k) for k in N]
times = [0] * len(X)

timing_i = 0
for x in X:
    setup = '''
from worksheets.ch02.lib import permutation_sort
'''
    exec = '''
permutation_sort({})
'''.format(x)
    
    times[timing_i] = min(timeit.repeat(stmt=exec, setup=setup, number=1, repeat=1)) * 1000
    timing_i += 1
    print('timing for n={} and x={}'.format(len(x), x))

[a, _] = curve_fit(model, np.array(N), np.array(times))

print('a: ', a)

table = DataTable([8, 15], ['N', 'time'])

N = [k for k in range(2, 21)]
for n in N:
    predicted_time = model(n, a[0])
    table.row([n, predicted_time])

# for training data = 10
# results show about 1180699062 years to permutation sort an n=50 list, worst case
# for training data = 12, 1710752886 years