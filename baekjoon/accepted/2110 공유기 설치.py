from sys import stdin


def solution(N, C, houses):
    houses.sort()

    def router_needed(min_gap):
        # to form min gap, n routers need to be installed
        installed = 1
        gap_start = houses[0]
        for h in houses[1:]:
            gap = h - gap_start
            if gap >= min_gap:
                installed += 1
                gap_start = h
        return installed

    s, e = 0, 1_000_000_000    # distance
    while s <= e:
        m = (s+e)//2

        if router_needed(m) >= C:
            s = m + 1
        else:
            e = m - 1
    return e


N, C, houses = 0, 0, []
for i,row in enumerate(stdin.readlines()):
    if i == 0:
        N, C = [int(c) for c in row.strip().split(' ')]
    else:
        houses.append(int(row))

print(solution(N, C, houses))