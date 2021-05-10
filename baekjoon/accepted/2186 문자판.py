from sys import stdin


def solution(N, M, K, board, word):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)

    alph_set = set(word)
    alphs = {}
    for x in range(N):
        for y in range(M):
            if board[x][y] in alph_set:
                alphs.setdefault(board[x][y], []).append((x, y))

    dp = [[[0]*len(word) for _ in range(M)] for _ in range(N)]
    for x, y in alphs[word[0]]:
        dp[x][y][0] = 1

    for i, char in enumerate(word[1:], 1):
        if char not in alphs:
            return 0

        for x, y in alphs[char]:
            for a in range(1, K+1):
                for dx, dy in DELTA:
                    nx, ny = a*dx + x, a*dy + y
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == word[i-1]:
                        dp[x][y][i] += dp[nx][ny][i-1]

    count = 0
    for x, y in alphs[word[-1]]:
        count += dp[x][y][-1]
    return count


N, M, K = map(int, stdin.readline().strip().split(' '))
board = [stdin.readline().strip() for _ in range(N)]
word = stdin.readline().strip()
print(solution(N, M, K, board, word))
