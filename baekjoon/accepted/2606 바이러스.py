from sys import stdin
from collections import deque

def solution(N, connections):
    routes = {}
    for this, that in connections:
        routes.setdefault(this, []).append(that)
        routes.setdefault(that, []).append(this)

    count = 0
    que, infected = deque([1]), {1}
    while que:
        computer = que.popleft()
        for other in routes[computer]:
            if other not in infected:
                infected.add(other)
                count += 1
                que.append(other)
    return count


N, connections = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    elif i == 1:
        continue
    else:
        connections.append([int(c) for c in row.strip().split(' ')])

print(solution(N, connections))