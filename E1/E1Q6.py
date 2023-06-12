# -*- coding: utf-8 -*-
"""
Experiment 1
Question 6

"""

import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0.0000001,1.2e7,int(1e4))
# n = np.linspace(0.0000001,8e5,int(1e4))

t_A = 2 * (n**2)/(10**10)
t_B = 50 * n * (np.log(n)/np.log(2))/(10**7)

a = 1e7
A = 2 * (a**2)/(10**10)
B = 50 * a * (np.log(a)/np.log(2))/(10**7)

plt.figure(3,figsize=(9,6))
plt.rc('font', size=20)  
plt.plot((n * 1e-4),t_A,color='red')
plt.plot((n * 1e-4),t_B,color='blue')
plt.scatter(x=[1000,1000], y=[A,B], c='g')

plt.xlabel('Amount of numbers x10 000')
plt.ylabel('Time taken (s)')
plt.title('Time VS n plot')
plt.grid()
plt.legend(['A', 'B'])
# plt.savefig("Q6b1",bbox_inches='tight')
