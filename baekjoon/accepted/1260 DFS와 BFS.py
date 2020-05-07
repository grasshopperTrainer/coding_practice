from sys import stdin
from collections import deque

def solution(N, M, V, routes):
    NOROUTE, ROUTE = 0, 1

    board = [[NOROUTE]*(N) for _ in range(N)]
    for x, y in routes:
        board[x-1][y-1] = ROUTE
        board[y-1][x-1] = ROUTE

    def dfs(pos, visited):
        record = [pos]
        for dest, is_routed in enumerate(board[pos]):
            if is_routed and dest not in visited:
                visited.add(dest)
                record += dfs(dest, visited)
        return record

    def bfs(pos):
        que = deque([pos])
        visited, record = {pos}, []
        while que:
            pos = que.popleft()
            record.append(pos)
            for dest, is_routed in enumerate(board[pos]):
                if is_routed and dest not in visited:
                    visited.add(dest)
                    que.append(dest)
        return record

    return dfs(V-1, {V-1}), bfs(V-1)


N, M, V, routes = 0, 0, 0, []
for i,row in enumerate(stdin.readlines()):
    row = [int(c) for c in row.strip().split(' ')]
    if i == 0:
        N, M, V = row
    else:
        routes.append(row)

for answer in solution(N, M, V, routes):
    print(' '.join(map(lambda x: str(x+1), answer)))