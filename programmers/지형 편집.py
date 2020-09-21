from math import ceil
import bisect


def solution(land, P, Q):
    land = sum(land, [])
    land.sort()
    N = len(land)
    RATIO = P/Q
    low, high = land[0], land[-1]
    while low <= high:
        target = (low+high)//2
        num_low, num_high = bisect.bisect_left(land,target), N - bisect.bisect_right(land, target)
        num_low = ceil(num_low*RATIO)
        if num_low < num_high:
            low, high = target+1, high
        else:
            low, high = low, target-1
    return sum([(low-l)*P if low > l else (l-low)*Q for l in land])



print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3))
print(solution([[1, 2], [2, 3]], 3, 2))
