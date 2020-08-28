from sys import stdin, setrecursionlimit
from collections import deque


setrecursionlimit(5000)
def solution(N, M, rels):
    students = [[0, set()] for _ in range(N)]
    for front, back in rels:
        students[back-1][0] += 1
        students[front-1][1].add(back-1)

    answer = []
    que = deque(i for i in range(N) if not students[i][0])
    while que:
        idx = que.popleft()
        answer.append(idx+1)
        for c in students[idx][1]:
            students[c][0] -= 1
            if not students[c][0]:
                que.append(c)
    return answer


N, M, rels = 0, 0, []
for i, row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M = row
    else:
        rels.append(row)

print(' '.join(str(i) for i in solution(N, M, rels)))

