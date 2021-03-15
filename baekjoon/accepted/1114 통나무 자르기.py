# quite confident but not accepted
from sys import stdin
import bisect
import heapq


def solution(L, K, C, cutables):
    cutables = [c for c in cutables if 0 <= c < L]
    cutables.sort()
    heap = [(-L, 0, L, cutables)]  # length, start, end

    blocks = []
    cut_count = 0
    while heap and cut_count != C:
        while heap and not heap[0][3]:  # if chunk has no cutting slot
            l, s, e, ___ = heapq.heappop(heap)
            cut = s if s != 0 else e
            blocks.append((l, cut))
        if heap:
            length, start, end, cand = heapq.heappop(heap)
            mid = (start + end) / 2

            # find closest to the center and decide where to cut
            i = bisect.bisect_left(cand, mid)
            if i == 0:
                m = cand[i]
                lcand, rcand = [], cand[1:]
            elif i == len(cand):
                m = cand[i - 1]
                lcand, rcand = cand[:i - 1], []
            elif mid - cand[i - 1] <= cand[i] - mid:  # ! equal direction
                # cut at i-1
                m = cand[i - 1]
                lcand, rcand = cand[:i - 1], cand[i:]
            else:
                # cut at i
                m = cand[i]
                lcand, rcand = cand[:i], cand[i + 1:]
            # print('cut at', m)
            heapq.heappush(heap, (-(m - start), start, m, lcand))
            heapq.heappush(heap, (-(end - m), m, end, rcand))
            cut_count += 1
    # left over
    for l, s, e, cand in heap:
        cut = s if s != 0 else e
        blocks.append((l, cut))
    blocks.sort()
    return f"{-blocks[0][0]} {blocks[0][1]}"


L, K, C = map(int, stdin.readline().strip().split(' '))
cutables = list(map(int, stdin.readline().strip().split(' ')))

print(solution(L, K, C, cutables))

"""
8 2 1
4 6
"""
"""
8 1 2
6
"""
"""
9 8 5
1 2 3 4 5 6 7 8
"""
"""
9 1 1
8
"""
"""
6 2 2
2 4
"""
"""
6 5 5
1 2 3 4 5
"""
"""
10 3 3
1 2 3
"""
"""
10 2 1
1 8
"""
"""
11 3 3
3 6 9
"""
"""
1000000000 3 3
3 6 9
"""
"""
3 3 3
1 6 9
"""
