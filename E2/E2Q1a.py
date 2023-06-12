# -*- coding: utf-8 -*-
"""
Experiment 2
Question 1
Part A

"""

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0.0000001,1e10,int(1e4))

best = 5 * n - 4
worst = (3/2) * (n**2) + n/2 -1


plt.figure(1,figsize=(9,6))
plt.rc('font', size=20)  
plt.plot(n,(best * 1e-3),color='red')
plt.legend('Best Case')

plt.figure(2,figsize=(9,6))
plt.plot(n,(worst * 1e-3),color='blue')
plt.legend('Worst Case')

plt.xlabel('Amount of numbers (n)')
plt.ylabel('Runtime (ms)')
plt.title('Runtime VS n plot')
plt.grid()
# plt.savefig("Q6b1",bbox_inches='tight')
