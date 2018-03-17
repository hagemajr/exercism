import time
import numpy as np

t = []

for x in range(100001):
    t.append(1)

def f1(l):
    for x in range(len(l)):
        if sum(l[:x]) == sum(l[x:]):
            return x
    return -1   

def f2(l):
    left_sum = 0
    right_sum = sum(l)
    for x in range(len(l)):
        if left_sum == right_sum:
            return x
        else:
            left_sum += l[x]
            right_sum -= l[x]
    return -1

print('starting first fn')
start_time = time.time()
print(f1(t))
print("--- %s seconds ---" % (time.time() - start_time))
print('starting 2nd fn')
start_time = time.time()
print(f2(t))
print("--- %s seconds ---" % (time.time() - start_time))

