from collections import deque


def solution(board):
    N = len(board)
    DELTA = ((1, 0),(-1, 0),(0, 1),(0, -1))
    BLOCKED = 1
    COST_S, COST_C = 100, 600


    dp = [[{d:float('inf') for d in DELTA} for _ in range(N)] for _ in range(N)]
    dp[0][0] = {d:0 for d in DELTA}
    que = deque([(0,0)])
    while que:
        x, y = que.popleft()
        for delta in DELTA:
            nx, ny = x + delta[0], y + delta[1]
            # minimal condition
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != BLOCKED:
                # check 3 candidates
                cand_cost = []
                for k, v in dp[x][y].items():
                    if k == delta:   # coming streight
                        cand_cost.append(v + COST_S)
                    else:  # coming prependicular
                        cand_cost.append(v + COST_C)

                if min(cand_cost) < dp[nx][ny][delta]:
                    dp[nx][ny][delta] = min(cand_cost)
                    que.append((nx, ny))

    return min(dp[-1][-1].values())

print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))