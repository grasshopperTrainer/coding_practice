from sys import stdin
from collections import deque


def solution(N, blocks):
    L = len(blocks)
    UNIT = N * 2 - 1

    def has_left(N, i):
        return not (i % UNIT == 0 or (i - N) % UNIT == 0)

    def has_right(N, i):
        return not ((i + N) % UNIT == 0 or (i + 1) % UNIT == 0)

    def has_below_left(N, i):
        if not N <= i:
            return False
        return i % UNIT != 0

    def has_below_right(N, i):
        if not N <= i:
            return False
        return (i + N) % UNIT != 0

    def has_above_left(N, i):
        if not i + N <= L:  # !critical, not `i + N < L`
            return False
        return i % UNIT != 0

    def has_above_right(N, i):
        if not i + N < L:
            return False
        return (i + N) % UNIT != 0

    record = [float('inf')] * L
    record[0] = 1

    farthest = 0  # for last not being reachable
    que = deque([(1, 0)])  # count, at
    while que:
        count, i = que.popleft()
        farthest = max(farthest, i)
        a, b = blocks[i]
        if has_left(N, i) and blocks[i - 1][1] == a and count + 1 < record[i - 1]:
            record[i - 1] = count + 1
            que.append((count + 1, i - 1))
        if has_right(N, i) and blocks[i + 1][0] == b and count + 1 < record[i + 1]:
            record[i + 1] = count + 1
            que.append((count + 1, i + 1))
        if has_below_left(N, i) and blocks[i - N][1] == a and count + 1 < record[i - N]:
            record[i - N] = count + 1
            que.append((count + 1, i - N))
        if has_below_right(N, i) and blocks[i - N + 1][0] == b and count + 1 < record[i - N + 1]:
            record[i - N + 1] = count + 1
            que.append((count + 1, i - N + 1))
        if has_above_right(N, i) and blocks[i + N][0] == b and count + 1 < record[i + N]:
            record[i + N] = count + 1
            que.append((count + 1, i + N))
        if has_above_left(N, i) and blocks[i + N - 1][1] == a and count + 1 < record[i + N - 1]:
            record[i + N - 1] = count + 1
            que.append((count + 1, i + N - 1))

    # from biggest deduct path
    path = []
    i = farthest
    while 0 < i:
        path.append(i + 1)
        a, b = blocks[i]
        # to left
        if has_left(N, i) and blocks[i - 1][1] == a and record[i - 1] == record[i] - 1:
            i = i - 1
            continue
        if has_right(N, i) and blocks[i + 1][0] == b and record[i + 1] == record[i] - 1:
            i = i + 1
            continue
        if has_below_left(N, i) and blocks[i - N][1] == a and record[i - N] == record[i] - 1:
            i = i - N
            continue
        if has_below_right(N, i) and blocks[i - N + 1][0] == b and record[i - N + 1] == record[i] - 1:
            i = i - N + 1
            continue
        if has_above_right(N, i) and blocks[i + N][0] == b and record[i + N] == record[i] - 1:
            i = i + N
            continue
        if has_above_left(N, i) and blocks[i + N - 1][1] == a and record[i + N - 1] == record[i] - 1:
            i = i + N - 1
            continue
    path.append(1)

    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))


N = int(stdin.readline())
blocks = [tuple(map(int, stdin.readline().strip().split(' '))) for _ in range(N ** 2 - N // 2)]
solution(N, blocks)

"""
2
5 5
5 1
1 5
"""
