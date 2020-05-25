import random
import time

NTRY = 100
times_sort = []
times_sort_reverse = []
for _ in range(NTRY):
    num = 1000000000
    n = num
    s = time.time()
    while n != 1:
        n >>= 1
    e = time.time()
    times_sort.append(e - s)

    n = num
    s = time.time()
    while n != 1:
        n //= 2
    e = time.time()
    times_sort_reverse.append(e - s)

print('shifting:        ', sum(times_sort)/len(times_sort))
print('division:', sum(times_sort_reverse)/len(times_sort_reverse))
# no difference