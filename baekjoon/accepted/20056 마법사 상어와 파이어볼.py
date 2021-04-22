from sys import stdin
from math import floor


def solution(N, M, K, balls):
    DELTA = (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)
    balls = list(map(lambda x: (x[0] - 1, x[1] - 1, *x[2:]), balls))
    for _ in range(K):

        poses = {}
        for x, y, m, s, d in balls:
            dx, dy = DELTA[d]
            nx, ny = (x + s * dx) % N, (y + s * dy) % N
            poses.setdefault((nx, ny), []).append((m, s, d))

        new_balls = []
        for (x, y), vals in poses.items():
            if len(vals) == 1:
                new_balls.append((x, y, *vals[0]))
                continue

            nm, ns, nd = 0, 0, []
            for m, s, d in vals:
                nm += m
                ns += s
                nd.append(d % 2)
            nm = floor(nm / 5)
            ns = floor(ns / len(vals))
            nd = (0, 2, 4, 6) if all(d == nd[0] for d in nd) else (1, 3, 5, 7)
            if nm != 0:
                for d in nd:
                    new_balls.append((x, y, nm, ns, d))

        balls = new_balls

    return sum(map(lambda x: x[2], balls))


lexer = lambda: list(map(int, stdin.readline().strip().split(' ')))
N, M, K = lexer()
balls = [lexer() for _ in range(M)]

print(solution(N, M, K, balls))
