from sys import stdin
from collections import deque


def solution(N, K, names):
    groups = {}
    for grade, name in enumerate(names):
        groups.setdefault(len(name), []).append((name, grade))

    count = 0
    for name_len, group in groups.items():
        que = deque()
        for name, grade in group:
            while que:
                if que[0] < grade - K:
                    que.popleft()
                else:
                    break
            count += len(que)
            que.append(grade)

    return count


N, K = map(int, stdin.readline().strip().split(' '))
names = [stdin.readline().strip() for _ in range(N)]
print(solution(N, K, names))