import time
from collections import deque

N = 1_000_00
sample_n = 10
_deque, _list = deque(range(N)), list(range(N))

times = []
for i in range(sample_n):
    start = time.time()
    while _deque:
        _deque.pop()
    end = time.time()
    times.append(end - start)
print('average execution of deque pop last:', sum(times)/sample_n)

times = []
for i in range(sample_n):
    start = time.time()
    while _list:
        _list.pop()
    end = time.time()
    times.append(end - start)
print('average execution of list pop last:', sum(times)/sample_n)


_deque, _list = deque(range(N)), list(range(N))

times = []
for i in range(sample_n):
    start = time.time()
    while _deque:
        _deque.popleft()
    end = time.time()
    times.append(end - start)
print('average execution of deque pop first:', sum(times)/sample_n)

times = []
for i in range(sample_n):
    start = time.time()
    while _list:
        _list.pop(0)
    end = time.time()
    times.append(end - start)
print('average execution of list pop first:', sum(times)/sample_n)
