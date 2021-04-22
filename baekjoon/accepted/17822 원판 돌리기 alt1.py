from sys import stdin
from collections import deque


def solution(N, M, T, disks, queries):
    ERASED = 0
    disks = [deque(disk) for disk in disks]
    for x, d, k in queries:
        # normalize rotation, find best rotation
        k = k % M
        k, d = min((k, d), (M - k, (d + 1) % 2))
        # rotate
        for disk in disks[x - 1:N:x]:
            for _ in range(k):
                if d == 0:
                    disk.appendleft(disk.pop())
                else:
                    disk.append(disk.popleft())

        # do dfs and erase values
        calc_average = True
        count = 0
        summed = 0
        visited = [[False] * M for _ in range(N)]
        for x, disk in enumerate(disks):
            for y, val in enumerate(disk):
                # ignore conditions
                if visited[x][y] or not val:
                    continue

                visited[x][y] = True
                que = deque([(x, y)])
                while que:
                    ox, oy = que.popleft()

                    any_erased = False
                    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                        nx, ny = ox + dx, (oy + dy) % M
                        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                            ov = disks[nx][ny]
                            if val == ov:
                                visited[nx][ny] = True
                                disks[nx][ny] = ERASED
                                any_erased = True
                                que.append((nx, ny))

                    if any_erased:
                        disks[x][y] = ERASED
                        calc_average = False
                    else:
                        summed += val
                        count += 1

        if calc_average:
            if count == 0:
                return 0
            ave = summed / count
            for disk in disks:
                for i, val in enumerate(disk):
                    if val == ERASED:
                        continue
                    if val < ave:
                        disk[i] += 1
                    elif ave < val:
                        disk[i] -= 1

    return sum(sum(disk) for disk in disks)


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, M, T = lexer()
disks = [lexer() for _ in range(N)]
queries = [lexer() for _ in range(T)]

print(solution(N, M, T, disks, queries))
