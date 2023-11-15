import random
import timeit
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from algs.table import DataTable
from ch02.bas import binary_array_search
from scipy.optimize import curve_fit







Ns = times = []
num = 50000




def log_model(n, a):
    return a * np.log2(n)

def time_bin_search(max_n): 
    trials = [2**k for k in range(5, max_n+1)]
    X = []
    Y = []

    for n in trials:
        setup='''
import random
from ch02.bas import binary_array_search
def generate_sorted_list(n):
    sampled_lst = random.sample(range(0, n*4), n)
    sorted_list = sorted(sampled_lst)
    return sorted_list
lst = generate_sorted_list({})
        '''
        exec= '''
binary_array_search(lst, {})
        '''    
        time = timeit.timeit(stmt=exec.format(random.randint(0, n * 4)), setup=setup.format(n), number=num)
        X.append(n)
        Y.append(time)
    return (X, Y)

(training_xs, training_ys) = time_bin_search(12)
[a, _] = curve_fit(log_model, np.array(training_xs), np.array(training_ys))

(real_xs, real_ys) = time_bin_search(24)
table = DataTable([8, 15, 15], ['n', 'real_time', 'model_time'])

for n in range(len(real_xs)):
    table.row([real_xs[n], real_ys[n], log_model(real_xs[n], a)[0]])

