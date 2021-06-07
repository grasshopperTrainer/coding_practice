from sys import stdin
import heapq


def solution(N, fishes):
    shark = [None, 2]  # pos, size
    for x in range(N):
        for y in range(N):
            if fishes[x][y] == 9:
                shark[0] = (x, y)
                fishes[x][y] = 0
                break

    total_count = 0
    eaten = 0
    while True:
        eat_fish = False

        # dijkstra to find closest
        moves = []
        moves.append((0, *shark[0]))  # count, at
        record = [[float('inf')] * N for _ in range(N)]
        while moves:
            count, x, y = heapq.heappop(moves)
            if 0 < fishes[x][y] < shark[1]:  # if fish eatable
                fishes[x][y] = 0
                eat_fish = True

                eaten += 1
                shark[0] = x, y
                total_count += count
                if eaten == shark[1]:
                    eaten = 0
                    shark[1] += 1
                break

            if record[x][y] <= count:
                continue
            record[x][y] = count

            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and fishes[nx][ny] <= shark[1] and count + 1 < record[nx][ny]:
                    heapq.heappush(moves, (count + 1, nx, ny))

        if not eat_fish:
            break
    return total_count


N = int(stdin.readline())
fishes = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]
print(solution(N, fishes))
