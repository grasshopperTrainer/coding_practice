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


def solution(N, M, T, D, carta):
    DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)
    carta = decode_carta(carta)

    max_height = 0
    record = [[float('inf')] * M for _ in range(N)]
    moves = [(0, 0, 0)]  # elapse time, go back time, height, x, y
    while moves:
        t_elapse, x, y = heapq.heappop(moves)
        # if t_elapse <= D:
        #     max_height = max(max_height, carta[])
        if record[x][y] <= t_elapse:
            continue
        record[x][y] = t_elapse

        height = carta[x][y]
        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and abs(carta[nx][ny] - height) <= T:
                if height < carta[nx][ny]:
                    t = (carta[nx][ny] - height) ** 2
                else:
                    t = 1
                if t + t_elapse < record[nx][ny]:
                    heapq.heappush(moves, (t + t_elapse, nx, ny))

    for row in carta:
        print(' '.join(map(lambda x: str(x).rjust(2), row)))
    print()

    for row in record:
        print(' '.join(map(lambda x: str(x).rjust(2), row)))

N, M, T, D = map(int, stdin.readline().strip().split(' '))
carta = [stdin.readline().strip() for _ in range(N)]
print(solution(N, M, T, D, carta))
