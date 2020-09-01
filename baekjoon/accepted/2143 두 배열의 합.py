from sys import stdin


def solution(T, N, M, series):
    # prepare sub sum series
    acounter, bcounter = {}, {}
    for counter, ser, l in zip((acounter, bcounter), series, (N, M)):
        for s in range(l):
            subsum = 0
            for e in range(s, l):
                subsum += ser[e]
                counter[subsum] = counter.get(subsum, 0) + 1

    count = 0
    for a, c in acounter.items():
        t = T-a
        if t in bcounter:
            count += bcounter[t]*c
    return count


T = int(stdin.readline())
N = int(stdin.readline())
series = []
series.append([int(c) for c in stdin.readline().strip().split(' ')])
M = int(stdin.readline())
series.append([int(c) for c in stdin.readline().strip().split(' ')])
print(solution(T, N, M, series))
