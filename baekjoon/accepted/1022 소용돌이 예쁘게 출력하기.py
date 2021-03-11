from sys import stdin


def solution(r0, r1, c0, c1):
    w, h = (c1 - c0 + 1), (r1 - r0 + 1)
    vs = [[None] * w for _ in range(h)]

    maxv = 0
    for x, r in enumerate(range(r0, r1 + 1)):
        for y, c in enumerate(range(c0, c1 + 1)):
            i = max(abs(r), abs(c))
            w = 2 * i + 1
            ref = w ** 2
            if r == i or c == -i:
                v = (ref - (i - r) - (i - c))
            else:
                v = (ref - (2 * w - 2) - (i + r) - (i + c))
            vs[x][y] = v
            maxv = max(maxv, v)

    length = len(str(maxv))
    for row in vs:
        print(' '.join(map(lambda v: str(v).rjust(length), row)))


r0, c0, r1, c1 = (int(i) for i in stdin.readline().strip().split(' '))
solution(r0, r1, c0, c1)

"""
-3 -3 3 3
"""
