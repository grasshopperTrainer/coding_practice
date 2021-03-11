from sys import stdin


def solution(N, M, board, K):
    MAXV = 2 ** N - 1
    cols = []
    for i in range(M):
        cols.append(int(''.join(v[i] for v in board), 2))

    def switch(coli, cols, k):
        if coli == len(cols):
            return 0
        if k == 0:
            v = MAXV
            for s in cols:
                v &= s
            return bin(v).count('1')

        # switch col and dont move
        cols[coli] = MAXV ^ cols[coli]
        a = switch(coli, cols, k - 1)
        # switch col and move
        b = switch(coli + 1, cols, k - 1)
        # dont switch and move
        cols[coli] = MAXV ^ cols[coli]
        c = switch(coli + 1, cols, k)
        return max(a, b, c)

    return switch(0, cols, K)


N, M = map(int, stdin.readline().strip().split(' '))
board = [stdin.readline().strip() for _ in range(N)]
K = int(stdin.readline())
print(solution(N, M, board, K))
