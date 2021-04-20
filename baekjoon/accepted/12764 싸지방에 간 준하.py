from sys import stdin
import heapq


def solution(users):
    users.sort()
    counter = {}
    heap = []
    seats = [1]
    for s, e in users:
        while heap and heap[0][0] < s:
            heapq.heappush(seats, heapq.heappop(heap)[1])
        if seats:
            seat = heapq.heappop(seats)
        else:
            seat = len(heap) + 1
        heapq.heappush(heap, (e, seat))
        counter[seat] = counter.get(seat, 0) + 1

    print(max(counter))
    print(' '.join(map(lambda x: str(x[1]), sorted(counter.items()))))

N = int(stdin.readline())
users = [list(map(int, stdin.readline().strip().split(' '))) for _ in range(N)]

solution(users)