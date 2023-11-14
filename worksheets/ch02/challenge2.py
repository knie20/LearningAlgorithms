import copy
import math
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit


from worksheets.ch02.lib import f4

def model(n, a, b):
    return a*(np.log2(np.log2(n))) + b

init_xs = [2**k for k in range(1, 5)]
init_ys = [f4(x) for x in init_xs]

[(a, b), _] = curve_fit(model, np.array(init_xs), np.array(init_ys))
print('Linear Model: {}*log(N) + {}'.format(a, b))

axis_x = [k for k in range(1, 50)]
input_xs = [2**k for k in axis_x]
input_ys = [f4(x) for x in input_xs]

fit_ys = [model(x, a, b) for x in input_xs]

x1 = np.array(axis_x)
y1 = np.array(input_ys)
x2 = np.array(axis_x)
y2 = np.array(fit_ys)

df = pd.DataFrame(data={
    'N': axis_x,
    'actual': input_ys,
    'fit': fit_ys
})

sns.set()

sns.lineplot(data=df, x='N', y='actual')
sns.lineplot(data=df, x='N', y='fit')

plt.show()
