import timeit
import matplotlib.pyplot as plt
import numpy as np


def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

def improved_func(n, memo={}):
  if n == 0 or n == 1:
    return n
  if n not in memo:
    memo[n] = improved_func(n-1, memo) + improved_func(n-2, memo)
  return memo[n]

first_attempt = []
second_attempt = []
X = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34]

for i in range(0,35):
    first_execution_time = timeit.timeit(lambda: func(i), number=1)
    first_attempt.append(first_execution_time)

for i in range(0,35):
    second_execution_time = timeit.timeit(lambda: improved_func(i), number=1)
    second_attempt.append(second_execution_time)

n=35
r = np.arange(n)
width = 0.25
  
  
# plt.bar(r, first_attempt, color = 'b',
#         width = width, edgecolor = 'black',
#         label='func()')
plt.bar(r + width, second_attempt, color = 'g',
        width = width, edgecolor = 'black',
        label='improved_func()')
  
plt.xlabel("Input to be computed")
plt.ylabel("Time (s)")
plt.title("Time taken to compute the fibonacci sequence")
  
plt.legend()
  
plt.show()