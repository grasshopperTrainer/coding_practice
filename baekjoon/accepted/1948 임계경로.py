from sys import stdin


def solution(n, m, edges, start, end):
    start, end = start - 1, end - 1

    count = [0] * n
    board = {}
    for s, e, c in edges:
        board.setdefault(s - 1, {})[e - 1] = c
        count[e - 1] += 1

    # do topological sorting and store max time
    que = [start]  # elapse time, count, at
    record = [0] * n
    while que:
        at = que.pop()
        for goto, goto_time in board.get(at, {}).items():
            if 0 <= goto_time:
                record[goto] = max(record[goto], record[at] + goto_time)

                count[goto] -= 1
                if count[goto] == 0:
                    que.append(goto)

    # count path
    road_count = 0
    visited = [False] * n
    que = [end]
    while que:
        at = que.pop()
        for come_from in range(n):
            if 0 <= board.get(come_from, {}).get(at, -1) and record[come_from] + board[come_from][at] == record[at]:
                road_count += 1
                if not visited[come_from]:
                    visited[come_from] = True
                    que.append(come_from)
    print(record[end])
    print(road_count)


n = int(stdin.readline())
m = int(stdin.readline())
edges = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(m)]
start, end = map(int, stdin.readline().strip().split(' '))

solution(n, m, edges, start, end)

"""
7
8
1 2 1
1 3 1
2 4 1
3 4 1
4 5 1
4 6 1
5 7 1
6 7 1
1 7
"""
