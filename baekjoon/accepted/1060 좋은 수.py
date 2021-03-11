from sys import stdin
import heapq


def solution(L, S, N):
    S.sort()

    groups = [(0, s, None, None, None, None, None) for s in S]  # set numbers has to also compete with 0 value numbers
    for i in range(len(S)):
        start = 1 if i == 0 else S[i - 1] + 1
        stop = S[i]

        base = stop - start - 1
        if base == -1:
            continue
        value = base
        number = start
        center = (start + stop) // 2
        heapq.heappush(groups, (value, number, start, stop, center, base, 0))  # value, number, start, stop, pointer

    answer = ''
    for i in range(N):
        if groups:  # have to check all groups
            val, num, start, stop, center, base, pointer = heapq.heappop(groups)
            answer += str(num) + ' '
            if start is not None and num != center:
                if 0 <= pointer:
                    pointer = -pointer - 1
                    num = stop + pointer
                    l = base + pointer + 1
                    r = base - l
                    val = base + (l * r)
                else:
                    pointer = -pointer
                    num = start + pointer
                    l, r = pointer, base - pointer
                    val = base + (l * r)
                heapq.heappush(groups, (val, num, start, stop, center, base, pointer))
        else:  # rest value infinity
            n = S[-1] + 1
            for j in range(i, N):
                answer += str(n) + ' '
                n += 1
            break

    print(answer.strip())


L = int(stdin.readline())
S = list(map(int, stdin.readline().strip().split(' ')))
N = int(stdin.readline())
solution(L, S, N)

"""
5
1 2 4 5 6
10
"""
"""
4
1 3 5 6
20
"""
"""
4
2 3 5 6
20
"""
"""
2
3 6
20
"""
"""
2
1
20
"""
"""
2
20
20
"""
"""
2
1 2 3 19 20
20
"""