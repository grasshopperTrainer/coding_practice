# dirty...
from sys import stdin


def solution(X, B):
    encoded = []

    if 0 < X:
        if 0 < B:
            negate = False
            flip_sign = False
            amp = 1
        else:
            negate = False
            flip_sign = True
            amp = 1
    else:
        if 0 < B:
            negate = True
            flip_sign = False
            amp = 1
        else:
            negate = False
            flip_sign = True
            amp = -1
    B = abs(B)
    X = abs(X)
    while X != 0:
        X, j = divmod(X, B*amp)
        encoded.append(abs(j))
        X = abs(X)
        if flip_sign:
            amp *= -1

    if not encoded:
        return 0
    else:
        v = int(''.join(map(str, reversed(encoded))))
        if negate:
            v = -v
        return v


print(solution(*map(int, stdin.readline().strip().split(' '))))
"""
6 2
"""
"""
110 -10
"""
"""
123456789 7
"""