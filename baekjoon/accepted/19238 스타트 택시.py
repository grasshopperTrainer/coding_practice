from sys import stdin
from collections import deque

DELTA = (-1, 0), (0, -1), (1, 0), (0, 1)


def calc_dists(carta, car, passengers):
    visited = [[False] * N for _ in range(N)]

    L = len(passengers)
    dists = []
    que = deque([(*car, 0)])
    while que:
        x, y, d = que.popleft()
        if visited[x][y]:
            continue

        visited[x][y] = True
        # if found
        if (x, y) in passengers:
            dists.append((d, (x, y)))  # dist, x, y, id
            if len(dists) == L:
                return dists

        for dx, dy in DELTA:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and carta[nx][ny] != 1:
                que.append((nx, ny, d + 1))

    return False


def solution(fuel, carta, car, passengers):
    car = car[0] - 1, car[1] - 1
    passengers = {(a, b): (c, d) for a, b, c, d in map(lambda x: map(lambda y: y-1, x), passengers)}

    for _ in range(len(passengers)):
        # find min dist passenger
        pick_dists = calc_dists(carta, car, passengers)
        if not pick_dists:
            return -1
        pick_dists.sort()
        pick_d, start = pick_dists[0]

        # find driving distance
        end = passengers[start]
        drive_d = calc_dists(carta, start, {end})
        if not drive_d:
            return -1
        drive_d, _ = drive_d[0]

        # find drivability
        total_d = pick_d + drive_d
        if total_d <= fuel:
            passengers.pop(start)
            car = end
            fuel = fuel - total_d + drive_d * 2
        else:
            return -1
    return fuel


parser = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, M, fuel = parser()
carta = [parser() for _ in range(N)]
car = parser()
passengers = [parser() for _ in range(M)]
print(solution(fuel, carta, car, passengers))
