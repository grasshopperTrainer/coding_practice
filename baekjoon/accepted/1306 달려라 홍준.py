from sys import stdin
import heapq


def solution(N, M, signs):
    brightests = []
    heap = []
    for i in range(2 * M - 1):
        heap.append((-signs[i], i))
    heapq.heapify(heap)
    brightests.append(-heap[0][0])

    for i in range(M, N - (M - 1)):
        head = signs[i+M-1]
        # put head
        heapq.heappush(heap, (-head, i+M-1))
        # pick brightest, but first, remove outdated
        while heap and heap[0][1] < i - (M - 1):
            heapq.heappop(heap)
        # pick brightest
        brightests.append(-heap[0][0])

    print(' '.join(map(str, brightests)))


N, M = map(int, stdin.readline().strip().split(' '))
signs = list(map(int, stdin.readline().strip().split(' ')))

solution(N, M, signs)

"""
10 3
1 2 1 2 3 3 4 1 2 6
"""
"""
10 3
1 2 3 2 1 2 3 2 1 2
"""
"""
10 1
1 2 1 2 3 3 4 1 2 6
"""
"""
5 3
1 1 1 3 2
"""