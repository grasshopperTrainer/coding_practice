from sys import stdin
import heapq


def decode_carta(carta):
    R, C = len(carta), len(carta[0])
    new_carta = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if carta[x][y].islower():
                new_carta[x][y] = 26 + ord(carta[x][y]) - ord('a')
            else:
                new_carta[x][y] = ord(carta[x][y]) - ord('A')
    return new_carta


def search_elapse_time(carta, T, easygo_qual):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)

    # first calculate go up
    record = [[float('inf')] * M for _ in range(N)]
    moves = [(0, 0, 0)]  # elapse time, height, x, y
    while moves:
        t_elapse, x, y = heapq.heappop(moves)
        if record[x][y] <= t_elapse:
            continue
        record[x][y] = t_elapse

        height = carta[x][y]
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and abs(carta[nx][ny] - height) <= T:
                if easygo_qual(height, carta[nx][ny]):
                    t = 1
                else:
                    t = (carta[nx][ny] - height) ** 2
                if t + t_elapse < record[nx][ny]:
                    heapq.heappush(moves, (t + t_elapse, nx, ny))
    return record


def solution(N, M, T, D, carta):
    carta = decode_carta(carta)

    up_record = search_elapse_time(carta, T, lambda x, y: x >= y)
    down_record = search_elapse_time(carta, T, lambda x, y: x <= y)

    max_height = 0
    for x in range(N):
        for y in range(M):
            total_elapse = up_record[x][y] + down_record[x][y]
            if total_elapse <= D:
                max_height = max(max_height, carta[x][y])
    return max_height


N, M, T, D = map(int, stdin.readline().strip().split(' '))
carta = [stdin.readline().strip() for _ in range(N)]
print(solution(N, M, T, D, carta))
