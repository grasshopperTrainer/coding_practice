from sys import stdin
from collections import deque


def solution(N, M, board):
    D = ((-1, 0), (0, -1), (1, 0), (0, 1))
    hpos = {}
    for x in range(N):
        for y in range(M):
            hpos.setdefault(board[x][y], []).append((x, y))

    def fill(height):
        count = 0
        checked = [[False]*M for _ in range(N)]
        for pos in hpos.get(height, []):
            if checked[pos[0]][pos[1]]:
                continue

            visited = [[False]*M for _ in range(N)]
            visited[pos[0]][pos[1]] = True
            que = deque([pos])
            fillable = True
            while que:
                x, y = que.popleft()
                for dx, dy in D:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if not visited[nx][ny]:
                            if board[nx][ny] == height:
                                visited[nx][ny] = True
                                que.append((nx, ny))
                            elif board[nx][ny] < height:
                                break
                    else:   # is not tightly bound no fill at all.
                        break
                else:
                    continue
                fillable = False
                break

            if fillable:
                c = 0
                for x in range(N):
                    for y in range(M):
                        if visited[x][y]:
                            hpos.setdefault(height+1, []).append(pos)
                            checked[x][y] = True
                            board[x][y] += 1
                            c += 1
                count += c
        return count

    return sum(fill(h) for h in range(1, 10))


N, M = map(int, stdin.readline().strip().split(' '))
board = [list(map(int, stdin.readline().strip())) for _ in range(N)]

print(solution(N, M, board))
