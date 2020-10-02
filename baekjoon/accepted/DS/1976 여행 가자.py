from sys import stdin


def find(node, ds):
    if ds[node] == node:
        return node
    ds[node] = find(ds[node], ds)
    return ds[node]


def union(a, b, ds):
    rs = [find(x,ds) for x in (a,b)]
    if rs[0] == rs[1]:
        return
    ds[rs[0]] = rs[1]


def solution(N, board, to_visit):
    ds = [i for i in range(N+1)]
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                union(i+1, j+1, ds)

    head = find(to_visit[0], ds)
    return ('NO', 'YES')[all([find(x, ds) == head for x in to_visit])]


N = int(stdin.readline())
M = int(stdin.readline())
board = [[int(c) for c in stdin.readline().strip().split(' ')] for _ in range(N)]
query = [int(c) for c in stdin.readline().strip().split(' ')]
print(solution(N, board, query))