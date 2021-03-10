from sys import stdin
from collections import deque
from math import isinf


def solution(N, ratios):
    edges = [[0]*N for _ in range(N)]
    # find one common value
    for a, b, p, q in ratios:
        pq_gcd = gcd(p, q)
        p, q = p//pq_gcd, q//pq_gcd
        edges[a][b] = (q, p)
        edges[b][a] = (p, q)

    values = [1]*N
    for i in range(N):
        while True:
            for goto, edge in enumerate(edges[at]):




def search(at, edges, values):
    que = deque([at])
    while que:
        at = que.popleft()
        for goto, edge in enumerate(edges[at]):
            if edge and isinf(values[goto]):
                a, b = edge
                if (values[at]*a) % b == 0:
                    values[goto] = (values[at]*a)//b
                    que.append(goto)
    return values


def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd(a, b):
    b, a = sorted([a, b])
    return b if a % b == 0 else gcd(b, a % b)


N = int(stdin.readline())
ratios = []
for _ in range(N - 1):
    ratios.append(list(map(lambda x: int(x), stdin.readline().strip().split(' '))))

print(' '.join(map(lambda x: str(x), solution(N, ratios))))
"""
5
1 0 9 9
1 4 3 1
1 2 5 1
1 3 7 1
"""

"""
3
0 1 2 3
0 2 5 2
"""

"""
4
0 1 3 2
1 3 4 8
2 3 9 9
"""
"""
4
0 1 9 8
1 3 7 6
2 3 5 3
"""
"""
4
0 1 1 1
0 3 1 1
0 2 1 1
"""

"""
10
0 1 7 5
0 3 2 3
0 2 8 9
3 4 2 5
5 6 2 1
2 6 4 6
7 8 2 9
2 1 3 5
1 3 2 7
"""

"""
2
0 1 9 1
"""
"""
3
0 1 2 3
1 2 5 7
"""