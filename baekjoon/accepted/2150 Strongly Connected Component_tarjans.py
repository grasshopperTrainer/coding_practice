# my solution
from sys import stdin, setrecursionlimit

setrecursionlimit(100_000)


def solution(V, E, from_to):
    graph = [[] for _ in range(V+1)]
    for f, t in from_to:
        graph[f].append(t)


V, E = [int(c) for c in stdin.readline().strip().split(' ')]
from_to = []
for _ in range(E):
    from_to.append([int(c) for c in stdin.readline().strip().split(' ')])

answer = solution(V, E, from_to)
print(len(answer))
for a in answer:
    print(f"{' '.join([str(i) for i in a])} -1")


"""
5 6
1 2
2 3
3 4
4 2
4 5
5 1
"""