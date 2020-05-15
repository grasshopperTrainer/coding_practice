from collections import deque


def solution(N, K):
    if N == K:
        return 0

    MOVES = lambda x: x+1, lambda x: x-1, lambda x: x*2
    MAX = min([max([N, K])*2, 100_000])

    visited = {N}
    que = deque([(N, 0)])
    while que:
        pos, time = que.popleft()
        for next_pos in map(lambda x, y: x(y), MOVES, [pos]*3):
            if next_pos == K:
                return time+1

            if next_pos not in visited and 0 <= next_pos <= MAX:
                que.append((next_pos, time+1))
                visited.add(next_pos)


N, K = [int(c) for c in input().strip().split(' ')]
print(solution(N, K))