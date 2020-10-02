from sys import stdin, setrecursionlimit

setrecursionlimit(1_000_100)


def find(node, ds):
    if ds[node] == node:
        return node
    ds[node] = find(ds[node], ds)
    return ds[node]


def union(a, b, ds):
    roots = [find(x, ds) for x in (a, b)]
    if roots[0] == roots[1]:
        return
    ds[roots[0]] = roots[1]


def solution(N, queries):
    ds = [i for i in range(N+1)]

    answers = []
    for op, a, b in queries:
        if op == 0:
            union(a, b, ds)
        elif op == 1:
            answers.append(('NO', 'YES')[find(a, ds) == find(b, ds)])
    return answers


N, M = [int(c) for c in stdin.readline().strip().split(' ')]
queries = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(M)]

for a in solution(N, queries):
    print(a)

"""
2 2
0 0 1
1 1 0

5 9
0 0 1
0 1 4
0 1 3
0 3 2
0 1 1
1 1 0
1 4 2
1 4 3
1 0 4

"""