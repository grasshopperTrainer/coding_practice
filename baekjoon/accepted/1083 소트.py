from sys import stdin


def solution(N, values, S):
    lp, rp = 0, 0

    gap = 0
    cand = {0: values[0]}
    while lp != N - 1 and S != 0:
        if gap < S:
            if rp < N - 1:  # if right can move farther
                rp += 1
                gap += 1
                cand[rp] = values[rp]
                continue
        if gap > S:  # right pointer retreat
            del cand[rp]
            gap -= 1
            rp -= 1
            continue

        # candidates all picked, find best among them
        # find biggest
        i, biggest = sorted(cand.items(), key=lambda x: x[1])[-1]
        if values[lp] < biggest:  # if its bigger, bring it to the front
            for k in range(i, lp, -1):  # bubble?
                values[k], values[k - 1], cand[k], cand[k - 1] = values[k - 1], values[k], cand[k - 1], cand[k]
            S -= (i - lp)
        # update candidates
        del cand[lp]
        lp += 1
        gap -= 1

    return ' '.join(map(str, values)).strip()


N = int(stdin.readline())
order = list(map(int, stdin.readline().strip().split(' ')))
S = int(stdin.readline())

print(solution(N, order, S))

"""
5
1 2 3 4 5
50
"""

"""
5
5 4 3 2 1
2
"""
"""
5
1 2 3 4 5
6
"""
