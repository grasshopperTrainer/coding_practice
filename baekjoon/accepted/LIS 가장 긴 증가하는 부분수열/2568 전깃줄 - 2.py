from sys import stdin


def solution(N, wires):
    def binary_search(arr, v):
        l, r = 0, len(arr)
        while l < r:
            mid = (r+l)//2
            if arr[mid] <= v:   # 같으면 안됨 같으면 한칸 위의 것을 확인해야 하기 때문에 <=
                l, r = mid+1, r
            else:
                l, r = l, mid
        return l

    # find LIS
    wires.sort(key=lambda x: x[0])
    series = [0] + [b for a, b in wires]
    LIS = [0]*(N+1)
    cache = [0]
    for i in range(1, N+1):
        pos = binary_search(cache, series[i])
        LIS[i] = pos
        if pos >= len(cache):
            cache.append(series[i])
        else:
            cache[pos] = series[i]
    l = len(cache)-1  # length searching for
    to_cut = []
    for i in range(N, 0, -1):
        if LIS[i] != l:
            to_cut.append(series[i])
        else:
            l -= 1

    # form answer
    b_idx = {b: a for a, b in wires}
    answer = [b_idx[b] for b in to_cut]
    answer.sort()
    return (len(answer), *answer)


N, wires = 0, []
for i, row in enumerate(stdin.readlines()):
    if i == 0:
        N = int(row)
    else:
        wires.append([int(c) for c in row.strip().split(' ')])

for a in solution(N, wires):
    print(a)

"""
3
1 1
2 2
3 3
"""
"""
3
1 2
2 3
3 1
"""
"""
4
1 2
2 1
3 4
4 3
"""