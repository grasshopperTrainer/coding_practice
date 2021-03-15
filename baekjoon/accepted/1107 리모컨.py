from sys import stdin


def solution(N, M, defected):
    current = 100
    L = len(str(N))

    disatnce = abs(N - current)
    if disatnce <= L:  # simple pressing works
        return disatnce

    offset = 0
    while True:
        for off in (-offset, offset):
            target = N + off
            if 0 <= target:
                disatnce = abs(current - target)
                if disatnce <= len(str(target)):  # if pressing +- is better than pressing numbers
                    return disatnce + abs(target - N)
                elif set(str(target)).isdisjoint(defected):
                    return len(str(target)) + abs(target - N)
        offset += 1


N = int(stdin.readline())
M = int(stdin.readline())
defected = set(stdin.readline().strip().split(' '))

print(solution(N, M, defected))

"""
0
10
0 1 2 3 4 5 6 7 8 9
"""