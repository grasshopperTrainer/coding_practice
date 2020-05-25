import random
import time

NTRY, NSAMPLE = 100000, 100
times_sort = []
times_sort_reverse = []
for _ in range(NTRY):
    nums = [random.randint(0, NSAMPLE) for i in range(NSAMPLE)]
    s = time.time()
    sorted(nums)
    e = time.time()
    times_sort.append(e - s)

    s = time.time()
    sorted(nums, reverse=True)
    e = time.time()
    times_sort_reverse.append(e - s)

print('sort:        ', sum(times_sort)/len(times_sort))
print('sort reverse:', sum(times_sort_reverse)/len(times_sort_reverse))
# result: depends on initial order?