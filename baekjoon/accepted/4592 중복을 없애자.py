from sys import stdin
from collections import deque


for row in stdin.readlines():
    if len(row.strip()) == 1:
        continue

    que = deque()
    for i, v in enumerate(row.strip().split(' ')):
        if i == 0:
            continue
        while que and que[-1] == v:
            que.pop()
        que.append(v)
    que.append('$')
    print(' '.join([str(i) for i in que]))